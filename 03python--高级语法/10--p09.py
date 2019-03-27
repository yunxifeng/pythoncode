import xml.etree.ElementTree as et

#在内存中创建一个空的文档
etree = et.ElementTree()
# 创建元素Student
e = et.Element('Student')
# 将Student设置为根
etree._setroot(e)
# 子元素Name
e_name = et.SubElement(e, 'Name')
# Name的值
e_name.text = "hahahah"
# 写入
etree.write('v06.xml')
