# 动态HTML--DHTML
   - JavaScript
   - jQuery
   - Ajax
## Python采集动态数据
- 1.从JavaScript代码入手采集
- 2.Python第三方库运行JavaScript,直接采集在浏览器看到的页面(主要)
## Selenium + PhantomJS
- Selenium: Web自动化测试工具
    - 安装: conda/pip install selenium==2.48
    - 官网: [http://selenium-python.readthedocs.io/index.html]
    - 一些功能: 
        - 自动加载页面
        - 获取数据
        - 截屏
- PhantomJS(幽灵): 基于Webkit的无界面浏览器
    - 安装: [http://phantomjs.org/download.html]
    - 官网: [http://phantomjs.org/download.html]
- 基本使用方法
    - Selenium+PhantomJS
    - Selenium参考资料: [http://www.cnblogs.com/zhaof/p/6953241.html]
        - Selenium库有一个WebDriver的API
        - WebDriver可以跟页面上的元素进行交互,用它来进行爬取
        - 案例: 06--p01.py
- 注: PhantomJS被chrome玩死了,所以下面用chrome(需要装上chromedriver驱动)
## Selenium+chrome(需要装上chromedriver驱动)
- Selenium操作主要分两大类:
    - 得到UI元素
        - find_element_by_id(通过id得到一个element元素)
        - find_elements_by_name
        - find_elements_by_path
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 通过导入ActionsChains类来实现以下操作
            - 单击
            - 右键
            - 拖拽
            - 输入
    - 案例: 06--p02.py
            
- 注: 自己玩玩或者工作量较小可以用浏览器这种模式,因为消耗资源太大