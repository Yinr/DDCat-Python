#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import logging

from sited.SitedPlug import SitedPlug


def main():
    parser = argparse.ArgumentParser(
        description='DDCat Plugin Tester',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file', help='plugin filename to test')
    parser.add_argument('-k', '--keyword', default='test',
                        help='keyword to test')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='show more infomation in runtime')
    args = parser.parse_args()

    if args.verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.INFO)

    sited = SitedPlug(args.file)

    print(sited.search_raw(args.keyword, '1'))
    print(sited.hots_raw('1'))


if __name__ == '__main__':
    main()
