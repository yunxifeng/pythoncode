# 正则表达式(Regular Expression, re)
- 是一个计算机科学的概念
- 用于使用单个字符串来描述,匹配符合某个规则的字符串
- 常常用来检索,替换某些模式的文本
## 正则的写法
- [http://www.runoob.com/regexp/regexp-metachar.html]
- .(点号): 表示任意一个字符,除了\n, 比如查找所有的一个字符 "\."
- []: 匹配中括号中列举的任意字符,比如[l, w, e], llw和well可以, lk不可以
- \d: 任意一个数字
- \D: 除了数字都可以
- \s: 表示空格, tab键
- \S: 除了空白符号
- \w: 单词字符, a-z, A-Z, 0-9, _
- \W: 除了单词字符, a-z, A-Z, 0-9, _
- *: 表示前面的内容重复零次或者多次, \w*: 表示可以有0个或多个单词字符
- +: 表示前面的内容至少出现一次
- ?: 匹配前面的子表达式零次或一次，
     或指明一个非贪婪限定符。
     要匹配 ? 字符，请使用 \?。
- {m,n}: 允许前面内容出现最少m次，最多n次
- ^: 匹配字符串的开始
- $: 匹配字符串的结尾
- \b: 匹配单词的边界
- (): 对正则表达式内容进行分组， 从第一个括号开始，编号逐渐增大      
- \A: 只匹配字符串开头， \Aabcd, 则abcd
- \Z: 仅匹配字符串末尾， abcd\Z, abcd
- |: 左右任意一个
- (?P<name>...): 分组，除了原来的编号再制定一个别名， (?P<id>12345){2}， 1234512345
- (?P=name): 引用分组，
- 案例:
        验证一个数字： ^\d$
        必须有一个数字，最少一位：^\d+$
        只能出现数字，且位数为5-10位： ^\d{5,10}$
        注册者输入年龄，要求16岁以上，99岁以下： ^[16-99]$
        只能输入英文字符和数字： ^[A-Za-z0-9]$
        验证qq号码： [0-9]{5,12}
# XPath
- 在XML文件中查找信息的一套规则/语言, 根据XML的元素或者属性进行遍历
- [http://www.w3school.com.cn/xpath/index.asp]
## XPath开发工具
- 开源的XPath表达式编辑工具: XMLQuire
- Chrome插件: XPath Helper
- Firefox插件: XPath Checker
## 选取节点
- nodename: 选取此节点的所有子节点
- /: 从根节点开始选取
     /Student:没有结果
     /School:选取School节点
- //: 选取节点, 不考虑位置
     //Age: 选取所有Age节点, 一般组成列表返回
- .: 选取当前节点
- ..: 选取当前节点的的父亲节点
- @: 选取属性
- XPath中查找一般按路径方法查找, 以下是路径表示方法
     School/Teacher: 返回Teacher节点
     School/Student: 返回两个Student节点
     //Student: 选取所有Student节点, 不考虑位置     
     School//Age: 选取School后代中所有Age节点
     //@Other: 选取Other属性
     //Age[@Detail]: 选取带有Detail属性的Age节点
## 谓语-Predicates
- /School/Student[1]: 选取School下面的第一个Student节点
- /School/Student[last()]: 选取School下面的最后一个Student节点
- /School/Student[last()-1]: 选取School下面的倒数第二个Student节点
- /School/Student[position()<3]: 选取School下面的前连个节点
- //Student[@score]: 选取带有属性score的Student节点
- //Student[@score="90"]: 选取带有属性score并且属性值是90的Student节点
- //Student[@score]/Age: 选取带有属性score的Student节点的子节点Age
## XPath的一些操作
- |：或者
     //Student[@score] | //Teacher: 选取带有属性score的Student节点或者Teacher节点
- 其余不常见的XPath运算符号
  - +, -, *, div, >, <






