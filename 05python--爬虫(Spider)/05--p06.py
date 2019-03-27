'''
lxml--解析HTML
'''
from lxml import etree

text = '''
<div>
    <ul>
       <li class="item-0"><a href="0.html">first item</a></li>  
       <li class="item-1"><a href="1.html">first item</a></li>
       <li class="item-2"><a href="2.html">first item</a></li>
       <li class="item-3"><a href="3.html">first item</a></li>
       <li class="item-4"><a href="4.html">first item</a>
    </ul>
</div>
'''
# 利用etree.HTML()把字符串解析成HTML文件
# 会自动补全html代码
html = etree.HTML(text)
s = etree.tostring(html)
print(s)



'''
lxml--XML文件读取
'''
html = etree.parse("./05--p05.xml")
print(type(html))
rst = etree.tostring(html, pretty_print=True)
print(rst)


'''
etree和XPath的配合使用
'''
html = etree.parse("./05--p05.xml")
print(type(html))

rst = html.xpath("//book")
print(type(rst))
print(rst)

rst = html.xpath("//book[@categary='cook']/price")
rst = rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)





