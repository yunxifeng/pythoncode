# 结构化文件存储
- xml,json
- 为了解决不同设备之间的信息交换问题
- xml:人可读,但是啰嗦
- json:更加简洁
## XML文件
- 参考资料:
   - [https://docs.python.org/3/library/xml.etree.elementtree.html]
   - [http://www.runoob.com/python/python-xml.html]
   - [https://blog.csdn.net/seetheworld518/article/details/49535285]
- XML(Extensible Markup Language):可扩展标记语言
   - 标记语言:语言中使用尖括号<>括起来的文本字符串标记
   - 可扩展:用户可以自己定义需要的标记
   - 例如:
         <Teacher> 
                自定义标记Teacher
                在两个标记之间任何内容都应该跟Teacher相关
            </Teacher>
   - 是W3C组织制定的一个标准
   - XML描述的是数据本身,即数据的结构和语义
   - HTML侧重于如何显示web页面中的数据,与运行平台无关
- XML文档的构成
   - 处理指令(可以认为一个文件只有一个处理指令)
      - <?xml version="1.0" encoding="UTF-8" ?>
      - 最多只有一行
      - 且必须在第一行
      - 内容是与xml本身处理相关的一些声明或指令
      - 以xml关键字开头
          - 一般用于声明XML的版本和采用的编码
          - version属性是必须的,版本号
          - encoding属性用来指出xml解释器使用的编码
   - 根元素(一个文件只有一个根元素)    
      - 在整个xml文件中,可以把它看做一个树形结构(只能有一棵树)
      -    <student>
               <name>hah</name>
               <age>18</age>
           </student>
      - 根元素: student
      - 根元素有且只能有一个
   - 子元素
      - 根元素下面的元素都是子元素
      - 如name,age
   - 属性
      - 对标签(元素)本身进行说明
      - <student type="" gender="" location="">
   - 内容
      - <name>hah</name>
      - 内容:hah
   - 注释
      - 起说明作用的信息
      - 规则:
         - 起说明作用的信息
         - 注释不能嵌套在标签里
         - 只有在注释的开始和结尾使用双短横线
         - 三短横线只能出现在注释的开头而不能用在结尾
        
                <name> <!-- wangdapeng -->   </name> #可以
                <name <!-- wangdapeng -->>   </name> #不可以，注释在标签内
                
                <!--my-name-by-wang--> #可以，注释内容可以有一个短横线
                <!--my--name--by--wang-->#不可以，双短横线只能出现在开头或结尾
                
                <!---my-name--> #可以， 三短横线只能出现在开头
                <!---my-name---> #不可以， 三短横线只能出现在开头
- 保留字符的处理
   - [https://blog.csdn.net/Holmofy/article/details/78130039] 
   - XML中使用的符号可能跟实际符号相冲突, 典型的就是左右尖括号
      - 错误示例: <score>math>80</score># 不能出现尖括号
   - 使用实体引用(EntityReference)来表示保留字符
      - 正确示例: <score>math&gt;80</score># 使用实体引用
      - 常用的需要转义的保留字符和对应实体引用:
         -  &lt;	<	小于
         -  &gt;	>	大于
         -  &amp;	&	和号
         -  &apos;	'	单引号
         -  &quot;	"	引号
   - 把含有保留字符的部分放在CDATA块内部, CDATA块把内部信息视为不需要转义
      - e.g.
           <![CDATA[
               select name, age
               from Student 
               where score>80
               ]]>
- XML标签的命名规则
   - Pascal命名法
   - 用单词表示, 第一个字母大写
   - 区分大小写
   - 配对的标签必须一致
- 命名空间
   - 为了防止命名冲突
       <Student type="" gender="" location="">
            <Name>hah</Name>
            <Age>18</Age>
            <Score>math>80</Score>
        </Student>
        <ClassRoom>
            <Name>2014</Name>
            <Location>1-23-1</Location>
        </ClassRoom>
   - 如果归并上述两个内容信息,会产生冲突,两个"Name"
       <Schooler>
            <Name>hah</Name>
            <Age>18</Age>
            <Score>math>80</Score>
     
            <Name>2014</Name>
            <Location>1-23-1</Location>
        </Schooler>
   - 为了避免冲突,需要给可能产生冲突的元素添加命名空间
       -xmlns: xml name space
       
        <Schooler xmlns:student="http://my_student" xmlns:classroom="http://my_classroom">
            <student:Name>hah</student:Name>
            <Age>18</Age>
            <Score>math>80</Score>
     
            <classroom:Name>2014</classroom:Name>
            <Location>1-23-1</Location>
        </Schooler>
### XML访问
- 读取:XML读取分主要两个技术, SAX, DOM
- SAX(Simple API for XML):
   - 基于事件驱动的API
   - 利用SAX解析文档涉及到解析器和事件处理两部分    
   - 特点:
      - 速度快
      - 流式读取(过去了就过去了,我不回头)
- DOM
   - 是W3C规定的XML编程接口
   - 一个XML文件在缓存中以树形结构保存,读取
      - (先读取解析,然后以树形结构保存在缓存中)
   - 用途:
      - 定位浏览XML任何一个节点信息
      - 添加删除相应内容
   - minidom包
      - minidom.parse(filename):            加载读取的xml文件, filename也可以是xml代码
      - doc.documentElement:                获取xml文档对象，一个xml文件只有一个对于的文档对象
      - node.getAttribute(attr_name):       获取xml节点的属性值
      - node.getElementByTagName(tage_name):得到一个节点对象集合
      - node.childNodes:                    得到所有孩子节点
      - node.childNodes[index].nodeValue:   获取单个节点值
      - node.firstNode:                     得到第一个节点，等价于node.childNodes[0]
      - node.attributes[tage_name]:         得到一个节点的所有属性值
   - etree包   
      - root = xml.etree.ElementTree.parse("xxx.xml")   以树形结构来表示xml
      - root.getiterator:                               得到相应的可迭代的node集合
      - root.iter
      - find(node_name):                                查找指定node_name的节点,返回一个node
      - root.findall(node_name):                        返回多个node_name的节点
      - node.tag:                                       node对应的tagename
      - node.text:                                      node的文本值
      - node.attrib：                                    是node的属性的字典类型的内容
### XML文件的写入
   - 更改
      - set:修改属性
      - append:添加子元素
      - remove:删除元素   
   - 生成创建
      - SubElement 
      - minidom写入
      - etree创建
## json
- 在线工具
   - [https://www.sojson.com/]
- 参考资料 
   - [http://www.w3school.com.cn/json/]
   - [http://www.runoob.com/json/json-tutorial.html]
- JSON(JavaScript Object Notation) 
   - 轻量级的数据交换格式,基于ECMAScript
   - json格式是一个键值对形式的数据集
      - key: 字符串
      - value: 字符串,数字,列表,json(说明json是可嵌套的)
      - json使用大括号包裹  
      - 键值对用逗号隔开
      - 例:
         student = {
            "name": "云汐风"
            "age": 18
            "mobile": 13693873438
             }
- json和python格式的对应
   - json : python
   - 字符串 : 字符串
   - 队列 : list
   - 对象 : dict
   - 布尔值 : 布尔值
- python for json
   - json包
   - json和python对象的转换
      - json.dumps(): 对数据编码,python格式->json格式
      - json.loads(): 对数据解码,json格式->python格式
   - python读取json文件
      - json.dump():把python文件内容写入json
      - json.load():把json文件内容写入python