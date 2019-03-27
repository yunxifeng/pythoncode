import xml.etree.ElementTree as et
# 生成元素Student1
stu = et.Element("Student1")
# 生成子元素Name
name = et.SubElement(stu, 'Name')
# Name的属性lang=en
name.attrib = {'lang','en'}
# Name的值
name.text = '云汐风'

# 生成子元素age
age = et.SubElement(stu, 'Age')
# age的值是18
age.text = 18

et.dump(stu)