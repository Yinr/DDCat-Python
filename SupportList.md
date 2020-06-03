# SiteD 插件语言支持列表

## 插件类型(dtype)
  - [ ] dtype=1, 漫画/有目录图片
  - [ ] dtype=2, 轻小说/小说
  - [ ] dtype=3, 动画/有目录视频
  - [ ] dtype=4, 图片/无目录漫画
  - [ ] dtype=5, 商品/周边/漫画书
  - [ ] dtype=6, 资讯/无目录小说
  - [ ] dtype=7, 视频/无目录动画
  - [ ] dtype=8, 工具
  - [ ] ~~加密插件(暂不考虑支持)~~

## 节点
  - [ ] meta, 头部节点
    - [x] ua, User-Agent
    - [ ] guid, 插件唯一标识
    - [x] title, 插件名称
    - [x] author, 插件开发者
    - [ ] contact, 插件开发者联系方式
    - [ ] intro, 插件介绍
    - [ ] alert, 插件提醒
    - [x] url, 源网站地址
    - [ ] expr, 匹配目标网址的正则表达式
    - [ ] logo, 插件图标
    - [ ] encoding, 目标网页默认编码
    - [ ] login, 登陆
    - [ ] about, 关于
  - [ ] main, 主体节点
    - [ ] home, 站点首页数据
      - [x] hots, 热门
        - [ ] updates, 更新
        - [ ] tags, 分类
        - [ ] item, 静态配置项
      - [x] updates, 更新
        - [ ] item, 静态配置项
      - [x] tags, 分类
        - [ ] item, 静态配置项
    - [x] search, 搜索
    - [ ] tag, 分类标签处理
    - [ ] subtag, 二级分类
    - [ ] book, 书本
      - [ ] sections
    - [ ] section, 章节
  - [x] script, 脚本节点
    - [x] require, 依赖脚本
      - [x] item
    - [x] code, 处理脚本

## 属性
### 根节点
  - [x] ver, 插件版本
  - [ ] vip?, 用户等级限制
  - [ ] debug?, 调试模式
  - [ ] private?, 私密插件
  - [ ] engine, 插件支持的引擎版本号
  - [ ] schema, 插件规范版本号
  - [ ] head?, 头部节点名称
  - [ ] body?, 主体节点名称
  - [ ] script?, 脚本节点名称
  - [ ] sds?, 自动更新接口

### main 主体节点
  - [ ] dtype, 数据类型
  - [ ] durl?, S 按钮打开的源网站地址
  - [ ] btype?, 业务类型
  - [ ] btag?, 对 btype 的真实描述
  - [ ] trace?, 插件点击记录请求网址

### Node 数据节点
  - [ ] cache, 缓存
  - [ ] title, 节点标题
  - [ ] ua, 节点 User-Agent
  - [ ] expr, 正则表达式
  - [ ] btn, 按钮名称
  - [ ] dtype, 节点内容类型
  - [ ] style, 界面样式风格
  - [ ] update, 数据更新方式
  - [ ] downAll, 允许全部下载
  - [ ] showNav, 上下集导航
  - [ ] showImg, 显示图片
  - [ ] showWeb, 显示 S 按钮
  - [ ] screen, 屏幕方向
  - [ ] options, 阅读选项（模式、方向、缩放、屏幕）
  - [ ] w, 宽比重
  - [ ] h, 高比重
  - [x] method, 请求方式
  - [ ] args, POST 请求数据
  - [x] parseUrl, 页面解析生成网址
  - [x] parse, 页面解析
  - [ ] check, 检查登陆状态
  - [ ] auto, 自动检查登陆状态
  - [x] buildUrl, 目标网址构建
  - [ ] buildWeb, 展示网址构建
  - [ ] buildRef, Referer 构建
  - [ ] buildArgs, POST 参数构建
  - [ ] buildHeader, Header 构建
  - [ ] buildCookie, Cookie 构建
  - [x] header, Header 参数
  - [ ] encode, 目标页面编码
  - [x] url, 目标网址
  - [ ] run, 为 `web` 时使用浏览器打开
  - [ ] addPage, 分页增加值
  - [ ] addKey, 搜索增加键
  - [ ] addCookie, 附加 Cookie

### Add 附加节点
  - [ ] parse, 解析函数
  - [ ] url, 目标网址
  - [ ] buildUrl, 目标网址构建

### Item 节点
  - [ ] title, 目标标题
  - [ ] group, 分组标题
  - [ ] url, 目标网址
  - [ ] text, 辅助文本

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

