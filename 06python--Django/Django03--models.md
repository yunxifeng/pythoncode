# models 模型
- 程序=数据结构+算法, 代码只是工具,用来实现数据结构和算法
- 数据库(DB)分类
- models相当于转接口
- ORM(Object Relation Map): 把面向对象思想转换成关系数据库思想.操作上把类等价于表格
    - 类对应表格
    - 类中的属性对应表中的字段
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是 models.Model 的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用 models.xxx 不能使用python中的类型
    - 在django中，Models负责跟数据库交互
- django链接数据库
    - 自带默认数据库Sqlite3
        - 关系型数据库
        - 轻量级
    - 建议开发用sqlite3，部署用mysql之类的数据库    
    - 具体操作:切换数据库在settings中进行设置 
       - 1.django连接mysql
            DATABASES = {
                 'default': { 
                 'ENGINE': 'django.db.backends.mysql', # 数据库引擎
                 'NAME': 'djangotest', #数据库名称 
                 'USER': 'root', # 链接数据库的用户名 
                 'PASSWORD': 'root', # 链接数据库的密码 
                 'HOST': '127.0.0.1', # mysql服务器的域名和ip地址 
                 'PORT': '3306', # mysql的一个端口号,默认是3306 
                 }
            }
       - 2.需要在项目文件下的__init__文件中导入pymysql包(第三方工具包,允许python代码访问mysql数据库)
        
                ```
                # 在主项目的__init__文件中
                import pymysql
                pymysql.install_as_MySQLdb()
                ```
# models类的使用
- 定义和数据库表映射的类
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是 models.Model 的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用 modles.xxx 不能使用python中的类型
- 字段常用参数
    1. max_length :      规定数值的最大长度
    2. blank :           是否允许字段为空,默认不允许
    3. null :            在DB中控制是否保存为null, 默认为false
    4. default :         默认值
    5. unique :          唯一
    6. verbose_name :    假名
# 数据库的迁移
- 即在数据库里生成跟models対应的表
   - 1. 在命令行中,生成数据迁移的语句(生成sql语句)

            ```
            # 准备迁移,准备sql语句
            python manage.py makemigrations
            ```
            
   - 2. 在命令行中,输入数据迁移的指令

            ```
            # 正式迁移,执行sql语句
            python manage.py migrate
            ```

            ps : 如果迁移中出现没有变化或者报错,可以尝试强制迁移

            ```
            # 强制迁移命令
            python manage.py makemigrations 应用名
            python manage.py migrate 应用名
            ```
   -  3. 对于默认数据库sqlite3，为了避免出现混乱，如果数据库中没有数据，每次迁移前可以把系统
         自带的sqlite3数据库删除(当执行迁移指令后,migrations会产生新文件,
         如果没有,就删除migration文件夹和sqlite3数据库<前提是数据库为空>,重新执行)
# 命令行操作数据库
   - 参考资料: [https://www.cnblogs.com/yangmv/p/5327477.html]
   - 注意: 对orm的操作分为静态函数和非静态函数两种.
           静态是指在内存中只有一份内容存在,调用的时候使用[ 类名. ]的方式.
           如果修改了那么所有使用的人都会受影响.
           非静态,通俗来说,是每个实例独有的,其他使用者不可以用
## 1.查看数据
   - 1. 启动命令行 : python manage.py shell
   - 2. 在命令行中导入对应的映射类
        from 应用.models import 类名
        e.g. from teacher.models import Teacher
   - 3. 使用 objects 属性操作数据库. objects 是 模型中实际和数据库进行交互的 Manager 类的实例化对象.
   - 4. 查询命令
        - 类名.objects.all() 查询数据库表中的所有内容. 
          e.g.Teacher.objects.all()
          - 只是调用了Teacher类的静态方法或静态变量,并没有实例化Teacher类,
            所有对数据库的操作都是通过ORM中的objects这个"代理"进行的
          - 返回的结果是一个QuerySet类型,实际上是类列表中装着一个一个数据对象.
        - 类名.objects.filter(条件) 
        '''
        基本操作
        >>> from teacher.models import Teacher
        >>> t = Teacher()
        >>> t.name = "云汐风"
        >>> t.age = 21
        >>> t.address = "河南"
        >>> t.course = "python"
        >>> t.save()
        >>> tt = Teacher.objects.all()
        >>> tt
        [<Teacher: Teacher object>]
        >>> type(tt)
        <class 'django.db.models.query.QuerySet'>
        >>> tt[0]
        <Teacher: Teacher object>
        >>> tt[0].name
        '云汐风'
        >>> tt[0].course
        'python'
         '''
         
         '''
         在models中加入魔法函数__str__
         >>> from teacher.models import Teacher
         >>> tt = Teacher.objects.all()
         >>> tt
         [<Teacher: 云汐风>]
         '''
         
         '''
         QuerySet类型类似于列表,是可迭代的,可以用for循环遍历
         >>> tt = Teacher.objects.all()
         >>> tt
         [<Teacher: 云汐风>, <Teacher: 李少白>, <Teacher: 狄仁杰>]
         >>> for i in tt:
         ...     print("Name:{0}, Age:{1}, Address:{2}, Course:{3}".format(i.name, i.age, i.address, i.course))
         ...
         Name:云汐风, Age:21, Address:河南, Course:python
         Name:李少白, Age:18, Address:江南, Course:Linux
         Name:狄仁杰, Age:16, Address:开封, Course:Web
         '''
         
         '''
         条件查询
         >>> aa = Teacher.objects.filter(age=18)
         >>> aa
         [<Teacher: 李少白>]     
         '''
   - 注: 思考如何使用for循环添加多条数据
   - (1)from 应用名.models import 类名
     from teacher.models import Teacher
    
   - (2)查询Teacher表中的所有数据,得到的是一个QuerySet类型
     Teacher.objects.all()
    
   - (3)如果要取出所有QuerySet类型中的所有数据对象,需要遍历取出所有的对象,再用对象.属性来查看值
     t = Teacher.object.all()
     for each in t:
        print(each.name , each.age , each.address , each.course)
    
   - (4)如果要进行过滤筛选,使用filter()方法
     Student.objects.filter(age=18)
## 2.添加数据
   - 对象 = 类()   # 使用类实例化对象
   - 对象.属性 = 值  # 给对应的对象的属性赋值
   - 对象.save()  # 必须要执行保存操作,否则数据没有进入数据库

   python manage.py shell 启动命令行

   - (1)from 应用名.models import 类名
     from teacher.models import Teacher
     
   - (2)实例化对象
     t = Teacher()
    
   - (3)给对象的属性赋值
     t.name = '云汐风'
     t.age = '21'
     t.address = '河南'
     t.course = python
    
   - (4)保存数据
     t.save()

## 常见查找方法
1. 通用查找格式: 属性名 _ _ (用下面的内容)  =值
    - gt :     大于
    - gte :    大于等于
    - lt :     小于
    - lte :    小于等于
    - range:   范围
    - year :   年份
    - isnull : 是否为空
- e.g. >>> t = Teacher.objects.filter(age__gt=18)
2. 查找等于指定值的格式: 属性名 = 值
3. 模糊查找:  属性名 _ _ (使用下面的内容) = 值
    - exact :    精确等于
    - iexact:    不区分大小写
    - contains:  包含
    - startwith: 以..开头
    - endwith:   以…结尾 
- >>> # 查找course中包含字母l的老师
  >>> t = Teacher.objects.filter(course__contains="l")

# 数据库表关系
- 多表联查：利用多个表联合查找某一项信息或者多项信息
- [https://blog.csdn.net/weixin_42470545/article/details/80784522]
- 注: 建议参看上述链接,以下笔记不全面,复习至此记得补全完善
## 1:1 One To One
  - 一.建立关系/添加数据
    - 1.建立关系：在模型任意一边即可，使用OneToOneField
       - e.g. my_school = models.OneToOneField(School)
    - 2.添加数据:  
       - 1.添加没有关系的一边，直接实例化保存就可以
        
            >>> s = School()
            >>> s.school_id = 2
            >>> s.school_name = "nanjingtulingxueyuan"
            >>> s.save()
            
       - 2.添加有关系的一边，使用create方法,或者使用实例化然后save
        
            # 添加方法1: 此种方法不建议
            >>> m = Manager()
            >>> m.manager_id = 10
            >>> m.manager_name = "dana"
            >>> m.my_school = s
            >>> m.save()
            
            # 添加方法2: 推荐
            >>> m = Manager.objects.create(manager_id=20, manager_name="erna", my_school=ss[0])
            - 此处my_school也可直接写作[my_school="xxx"]
  - 二.查询数据/更改数据
    - 1.查询数据(query):
        - 1.由子表查母表：由子表的属性直接提取信息
        - 已知manager_name,查询manager所在school的school_name
        >>> m = Manager.objects.get(manager_name="dana")
        >>> m
        <Manager: dana>
        >>> type(m.my_school)
        <class 'relate.models.School'>
        >>> m.my_school.school_name
        '北京图灵学院'
        - 或者: 串联操作
        >>> m = Manager.objects.get(manager_name="dana").my_school.school_name
        >>> m
        '北京图灵学院'
        - 2.由母表查子表：使用双下划线 
        - 写法:母表.objects.get(子表名小写__子表字段=‘xxx')
        - 已知一个manager的manager_name="dana",得到所在school
        '''
        >>> s = School.objects.get(manager__manager_name="dana")
        >>> s
        <School: 北京图灵学院>
        '''
    - 2.更改数据(change):
       - 1.单个修改使用save  
            >>> s
            <School: 北京图灵学院>
            >>> s.school_name
            '北京图灵学院'
            >>> ss = School.objects.all()
            >>> ss
            [<School: 北京图灵学院>, <School: 郑州大学>]
            >>> s.school_name="图灵学院"
            >>> s.save()
            >>> s
            <School: 图灵学院>   
       - 2.批量修改使用update
            >>> ss
            [<School: 图灵学院>, <School: 郑州大学>]
            >>> type(ss)
            <class 'django.db.models.query.QuerySet'>
            >>> ss.update(school_name="图灵学院")
            2
            >>> ss
            [<School: 图灵学院>, <School: 图灵学院>]
       - 3.无论对子表还是对母表的修改,都是以上方法
    - 三.删除数据(delete)
       - 直接使用delete()删除   
       - e.g.
         models.UserInfo.objects.filter(user='yangmv').delete()   
        
    
## 1:N One To Many
  - 一个表格的一个数据项/对象等，可以有很多个另一个表格的数据项
    - 比如：一个学校可以有很多个老师，但一个老师只能在一个学校里上班
  - 一.建立联系/添加数据 
    - 1.建立联系:
        - 使用ForengnKey
        - 在多的那一边，比如上边的例子就是在Teacher的表格里进行定义        
    - 2.添加数据:
        - 跟一对一方法类似，通过create和new来添加
        - create: 把属性都填满，然后不需要手动保存
        - new: 属性或者参数可以为空，此时不检查约束,必须用save保存,一旦保存,就会检查约束
  - 二.查询数据(query): 
        - 以学校和老师的例子为准
        - 1.如果知道老师查学校,则通过增加的关系属性，直接使用 
        - 例如，查找t1老师是哪个学校的
            '''
            >>> t1
            <Teacher: 刘大拿>
            >>> t1.tea_school
            <School: 图灵学院>
            '''
        - 2.反查: 已知学校查找老师
                  一对多,系统会自动在学校类(School)中添加属性(???不确定是不是属性):类名(小写,teacher)_set
                  用来表示
                 e.g. 某学校.teacher_set.all(): 显示该学校下所有老师

## N:N Many To Many   
 - 表示任意一个表的数据可以拥有对方表格多项数据，反之亦然
 - 比如典型例子就是老师和学生的关系
 - 一.建立联系/添加数据   
    - 1.建立联系
        - 使用上，在任意一方，使用ManyToMany定义，只需要定义一边
    - 2.添加数据:
        - 添加老师，则在student.teachers.add()
        >>> t1 = Teacher.objects.all()[0]
        >>> s1 = Student()
        >>> s1.student_name="yunxifeng"
        >>> s1.save()
        >>> s1.teachers.add(t1)
        >>> s1.save()
        >>> s1.teachers.all()
        [<Teacher: 刘大拿>]
        
    二.查询数据(Query):
        - 跟一对多类似，使用_set查询
        - e.g.已知老师,查找所有学生
          - t1.student_set.all()
    