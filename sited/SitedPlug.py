# -*- coding: utf-8 -*-

import os
import logging

import requests
import xml.etree.ElementTree as ET
from py_mini_racer import py_mini_racer


class SitedPlug(object):
    def __init__(self, filepath: str):
        if not os.path.isfile(filepath):
            logging.error('Plugin file({}) is not exist'.format(filepath))
            return
        logging.info('parse plugin file: {}'.format(filepath))
        self.etree = ET.parse(filepath)
        logging.info('plugin title: {}, '
                     'Author: {}, '
                     'version: {}, '
                     'engine: {}'.format(
                         self.etree.find('./meta/title').text,
                         self.etree.find('./meta/author').text,
                         self.etree.getroot().attrib['ver'],
                         self.etree.getroot().attrib['engine']))
        self.prepare()

    def prepare(self):
        self.url = SitedRequest()
        uaTag = self.etree.find('./meta/ua')
        self.url.set_headers(
            'user-agent',
            uaTag.text if uaTag is not None and uaTag.text is not None
            else 'dct')
        self.prepare_js()

    def prepare_js(self):
        logging.info('prepare js runtime')
        js_tag = self.etree.find('./{}'.format(
            self.etree.getroot().attrib.get('script', 'script')))
        self.js = py_mini_racer.MiniRacer()
        for item in js_tag.findall('./require/item'):
            libcode = self.url.get(item.attrib['url'])
            logging.info('load script require: {}'.format(item.attrib['url']))
            self.js.eval(libcode)
        logging.info('load script')
        self.js.eval(js_tag.find('./code').text)
        self.js.eval('SiteD = {}')  # TODO 导入 SiteD 全局变量

    def getNodeData(self, node_info: dict, keys=dict(), url=None) -> list:
        """get parsed data of a Node

        Arguments:
            node_info (dict): dictionary type of the node attributes
            keys (dict): dictionary type of url params like keywords and page
            url (str): url while not get the default url within node_info,
                       or while there's no url in node_info

        Returns:
            list: the list of a json string which according to dtypes
        """
        url = node_info.get('url') if url is None else url
        url = url.replace('@key', keys.get('keyword', ''))
        url = url.replace('@page', keys.get('page', ''))
        if type(node_info) == ET.Element:
            logging.info('getNodeData of {}'.format(node_info.tag))
        logging.debug('getNodeData with url: {}'.format(url))
        if node_info.get('buildUrl') is not None:
            url = self.js.call(node_info.get('buildUrl'), url)
            logging.info('build url to: {}'.format(url))
        if node_info.get('parseUrl') is not None:
            url = self.__parseUrl(node_info, url,
                                  keys.get('keyword', ''),
                                  keys.get('page', '1'))
            logging.info('parse url to: {}'.format(url))
        return [self.js.call(node_info.get('parse'), iurl,
                             self.url.query(iurl, node_info))
                for iurl in url.split(';')]

    def __parseUrl(self, node_info: dict, url: str) -> str:
        res = self.url.query(url, node_info)
        urls = self.js.call(node_info.get('parseUrl'), url, res)
        if 'CALL::' in urls:
            for item in [url for url in urls.split(';')
                         if url.startswith('CALL::')]:
                self.__parseUrl(node_info, item[6:])

    def search_raw(self, keyword: str, page='1') -> list:
        searchTag = self.etree.find('./main/search')
        return self.getNodeData(searchTag, {'keyword': keyword, 'page': page})

    def hots_raw(self, page='1') -> list:
        hotsTag = self.etree.find('./main/home/hots')
        return self.getNodeData(hotsTag, {'keyword': '', 'page': page})


class SitedRequest():
    def __init__(self):
        self.headers = {}
        self.cookies = {}

    def query(self, url, query_info=dict(), data=dict()) -> str:
        method = query_info.get('method', 'get').lower()
        headers = query_info.get('header', '').split(" $$ ")

        if url.startswith('GET:'):
            method = 'get'
            url = url[4:]
        elif url.startswith('POST:'):
            method = 'post'
            url = url[5:]

        if method == 'get':
            return self.get(url, headers)
        elif method == 'post':
            return self.get(url, data, headers)
        elif method == '@null':
            return url

    def get(self, url: str, headers=[]) -> str:
        headers = self.get_headers(headers)
        cookies = self.cookies if 'cookie' in headers else {}
        logging.info('GET url: {}'.format(url))
        r = requests.get(url, headers=headers, cookies=cookies)
        logging.debug('GET url with code: {}'.format(r.status_code))
        logging.debug('GET url result: {}'.format(r.text))
        self.set_cookies(r.cookies)
        return(r.text)

    def post(self, url: str, data=dict(), headers=[]) -> str:
        headers = self.get_headers(headers)
        cookies = self.cookies if 'cookie' in headers else {}
        logging.info('POST url: {}'.format(url))
        r = requests.post(url, data=data, headers=headers, cookies=cookies)
        logging.debug('POST url with code: {}'.format(r.status_code))
        logging.debug('POST url result: {}'.format(r.text))
        self.set_cookies(r.cookies)
        return(r.text)

    def set_headers(self, key: str, value: str):
        self.headers[key] = value

    def get_headers(self, keys: list) -> dict:
        res_headers = {}
        mod_keys = keys + ['user-agent']
        for item in mod_keys:
            if ':' in item:
                key, value = item.split(':')
                self.set_headers(key, value)
            elif '=' in item:
                key, value = item.split('=')
                self.set_headers(key, value)
            elif 'cookie' == item:
                pass
            else:
                res_headers[item] = self.headers.get(item)
        return res_headers

    def set_cookies(self, cookies: dict):
        self.cookies.update(cookies)
