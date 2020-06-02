# SiteD 插件语言支持列表

## 插件类型(dtype)
  - [ ] dtype=1
  - [ ] dtype=2
  - [ ] dtype=3
  - [ ] dtype=4
  - [ ] dtype=5
  - [ ] dtype=6
  - [ ] dtype=7
  - [ ] dtype=8
  - [ ] ~~加密插件(暂不考虑支持)~~

## 节点
  - [ ] meta, 插件信息
    - [x] ua, User-Agent
    - [ ] guid
    - [x] title, 插件名称
    - [x] author, 插件作者
    - [ ] contact
    - [ ] intro
    - [ ] alert
    - [x] url, 插件主页
    - [ ] exper
    - [ ] logo, 插件图标
    - [ ] encoding, 插件网页编码
    - [ ] login, 登陆信息
    - [ ] about
  - [ ] main
    - [ ] home, 主界面
      - [x] hots, 排行榜
        - [ ] updates
        - [ ] tags
      - [x] updates, 最近更新
      - [x] tags, 分类标签
    - [x] search, 搜索
    - [ ] tag, 分类标签处理
    - [ ] subtag
    - [ ] book
      - [ ] sections
    - [ ] section
  - [x] script, 脚本
    - [x] require, 依赖脚本
      - [x] item
    - [x] code, 处理脚本

## 属性
### 根节点
  - [x] ver, 插件版本
  - [ ] vip?, VIP 类型
  - [ ] debug?, 调试模式
  - [ ] private?, 私有插件
  - [ ] engine, 插件引擎版本
  - [ ] schema, 插件规范
  - [ ] head?, 插件信息标签名
  - [ ] body?, 插件界面标签名
  - [ ] script?, 插件脚本标签名
  - [ ] sds?

### main 节点
  - [ ] dtype
  - [ ] durl
  - [ ] btype
  - [ ] btag
  - [ ] trace

### Node 节点
  - [ ] cache
  - [ ] title
  - [ ] ua
  - [ ] expr
  - [ ] btn
  - [ ] dtype
  - [ ] style
  - [ ] update
  - [ ] downAll
  - [ ] showNav
  - [ ] showImg
  - [ ] showWeb
  - [ ] screen
  - [ ] options
  - [ ] w
  - [ ] h
  - [x] method
  - [ ] args
  - [x] parseUrl
  - [x] parse
  - [ ] check
  - [ ] auto
  - [x] buildUrl
  - [ ] buildWeb
  - [ ] buildRef
  - [ ] buildArgs
  - [ ] buildHeader
  - [ ] buildCookie
  - [x] header
  - [ ] encode
  - [x] url
  - [ ] run
  - [ ] addPage
  - [ ] addKey
  - [ ] addCookie

### Item 节点
  - [ ] title
  - [ ] group
  - [ ] url
  - [ ] text

### Add 节点
  - [ ] parse
  - [ ] url
  - [ ] buildUrl

## 全局变量
  - [ ] SiteD
    - 属性
      - [ ] ver, SiteD 引擎版本
      - [ ] udid, 用户设备 ID
      - [ ] uid, 用户 ID
      - [ ] usex, 用户性别
      - [ ] uvip, 用户 VIP 类型
      - [ ] ulevel, 用户等级
    - 方法
      - [ ] get, 获取全局变量
      - [ ] set, 设置全局变量
    - API
      - [ ] get('g_location'), 获取当前定位

