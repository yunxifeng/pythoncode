# 模板系统
- 模板: 一组相同或相似的页面,在需要个性化的地方留白,在需要用的时候用数据渲染
- 步骤: 
   - 1.在settings中进行设置模板路径:TEMPLEATS
     - 'DIRS': [os.path.join(BASE_DIR,"templates")],
   - 2.在templates下编写模板并调用
## 模板--变量
- 变量的表示方法: {{变量名}}
- 在系统调用模板的时候,会用相应的数据查找相应的变量名称，如果能找到，则填充(渲染)，否则，跳过不报错
## 模板--标签
- 1.for标签
    - 用法：
        {% for .. in .. %}
            循环语句
        {% endfor %}
    - 在标签中添加 reversed，反向迭代列表：
        {% for athlete in athlete_list reversed %}
        ...
        {% endfor %}     
    - {% for %} 标签可以嵌套：
        {% for athlete in athlete_list %}
        <h1>{{ athlete.name }}</h1>
        <ul>
            {% for sport in athlete.sports_played %}
            <li>{{ sport }}</li>
            {% endfor %}
        </ul>
        {% endfor %}    
    - 如果需要迭代由列表构成的列表，可以把每个子列表中的值拆包到独立的变量中。dict也可以
        - 比如说上下文中有一个包含 (x,y) 坐标点的列表，名为 points
        {% for x, y in points %}
        <p>There is a point at {{ x }},{{ y }}</p>
        {% endfor %}
        - dict
        {% for key, value in data.items %}
        {{ key }}: {{ value }}
        {% endfor %}
    - 通常，迭代列表之前要先检查列表的大小
        {% for athlete in athlete_list %}
        <p>{{ athlete.name }}</p>
        {% empty %}   // 用于定义列表为空时显示的内容
        <p>There are no athletes. Only computer programmers.</p>
        {% endfor %}
    - 在循环结束之前，无法“跳出”。也没有“continue”语句
    
    - 在 {% for %} 循环内部，可以访问一个名为 forloop 的模板变量。这个变量有几个属性，通过它们可以获知
      循环进程的一些信息：
        • forloop.counter 的值是一个整数，表示循环的次数。这个属性的值从 1 开始，因此第一次循环时，
                forloop.counter 等于 1。下面举个例子：
                {% for item in todo_list %}
                <p>{{ forloop.counter }}: {{ item }}</p>
                {% endfor %}
        
        • forloop.counter0 与 forloop.counter 类似，不过是从零开始的。第一次循环时，其值为 0。
        • forloop.revcounter 的值是一个整数，表示循环中剩余的元素数量。第一次循环时，forloop.revcounter 的值是序列中要遍历的元素总数。最后一次循环时，forloop.revcounter 的值为 1。
        • forloop.revcounter0 与 forloop.revcounter 类似，不过索引是基于零的。第一次循环时，forloop.revcounter0 的值是序列中元素数量减去一。最后一次循环时，forloop.revcounter0 的值为 0。
        • forloop.first 是个布尔值，第一次循环时为 True。需要特殊处理第一个元素时很方便：
                {% for object in objects %}
                {% if forloop.first %}
                <li class="first">
                {% else %}
                <li>
                {% endif %}
                {{ object }}
                </li>
                {% endfor %}
        • forloop.last 是个布尔值，最后一次循环时为 True。经常用它在一组链接之间放置管道符号：
                {% for link in links %}
                {{ link }}{% if not forloop.last %} | {% endif %}
                {% endfor %}
                上述模板代码的输出可能是：
                Link1 | Link2 | Link3 | Link4
                此外，还经常用它在一组单词之间放置逗号：
                <p>Favorite places:</p>
                {% for p in places %}
                {{ p }}{% if not forloop.last %}, {% endif %}
                {% endfor %}
        • 在嵌套的循环中，forloop.parentloop 引用父级循环的 forloop 对象。下面举个例子：
                {% for country in countries %}
                <table>
                {% for city in country.city_list %}
                <tr>
                <td>Country #{{ forloop.parentloop.counter }}</td>
                <td>City #{{ forloop.counter }}</td>
                <td>{{ city }}</td>
                </tr>
                {% endfor %}
                </table>
                {% endfor %}
        forloop 变量只在循环内部可用。模板解析器遇到 {% endfor %} 时，forloop 随之消失。
    -  {% ifequal %} 标签比较两个值，如果相等，显示 {% ifequal %} 和 {% endifequal %} 之间的内容。下述示例
        比较模板标签 user 和 currentuser：
                {% ifequal user currentuser %}
                <h1>Welcome!</h1>
                {% endifequal %}
        参数可以是硬编码的字符串，使用单引号或双引号都行，因此下述代码是有效的：
                {% ifequal section 'sitenews' %}
                <h1>Site News</h1>
                {% endifequal %}
                {% ifequal section "community" %}
                <h1>Community</h1>    
                {% endifequal %}
        与 {% if %} 一样，{% ifequal %} 标签支持可选的 {% else %} 子句：
                {% ifequal section 'sitenews' %}
                <h1>Site News</h1>
                {% else %}
                <h1>No News Here</h1>
                {% endifequal %}
        {% ifequal %} 的参数只能是模板变量、字符串、整数和小数。下面是有效的示例：
                {% ifequal variable 1 %}
                {% ifequal variable 1.23 %}
                {% ifequal variable 'foo' %}
                {% ifequal variable "foo" %}
        其他变量类型，例如 Python 字典、列表或布尔值，不能在 {% ifequal %} 中硬编码。下面是无效的示例：
                {% ifequal variable True %}
                {% ifequal variable [1, 2, 3] %}
                {% ifequal variable {'key': 'value'} %}
        ifequal 标签可以替换成 if 标签和 == 运算符。
        {% ifnotequal %} 的作用与 ifequal 类似，不过它测试两个参数是否不相等。ifnotequal 标签可以替换成 if
        标签和 != 运算符。
          
- 2.if标签 
    - 用法:
        {% if 条件 %}
            条件成立执行语句
        {% elif 条件 %}}
            条件成立执行语句
        {% else %}
            以上条件都不成立执行语句
        {% endif %}}
    - {% if %} 支持使用 and、or 或 not 测试多个变量，或者取反指定的变量。例如：
        {% if athlete_list and coach_list %}
            <p>Both athletes and coaches are available. </p>
        {% endif %}
    - 通过嵌套if标签指定运算优先级
        {% if athlete_list %}
            {% if coach_list or cheerleader_list %}
                <p>We have athletes, and either coaches or cheerleaders! </p>
            {% endif %}
        {% endif %}    
    - 注: 在 if 标签中使用括号是无效的句法。
    - 注: 多次使用相同的逻辑运算符没问题，但是不能混用不同的运算符。
        {% if athlete_list or coach_list or parent_list or teacher_list %}
    
 
- 3.csrf标签
    - [https://www.aliyun.com/jiaocheng/436463.html?spm=5176.100033.2.7.3da91713Q2qX7b]
    - [https://www.cnblogs.com/shytong/p/5308667.html]
    - CSRF（Cross-site request forgery）跨站请求伪造  
    - 为防范CSRF攻击,在提交表单的时候,表单页面必须加上{% csrf_token %}   
    
- 4.注释
    与 HTML 和 Python 一样，Django 模板语言支持注释。注释使用 {# #} 标明：
        {# This is a comment #}
    渲染模板时，不输出注释。使用这种句法编写的注释不能分成多行。这一限制有助于提升模板解析性能。
    在下述模板中，渲染的结果与模板完全一样（即注释标签不会解析为注释）：
        This is a {# this is not
        a comment #}
        test.
    如果想编写多行注释，使用 {% comment %} 模板标签，如下所示：
        {% comment %}
        This is a
        multi-line comment.
        {% endcomment %}
    注释标签不能嵌套
- 5.过滤器
    - 模板过滤器是在显示变量之前调整变量值的简单方式。过滤器使用管道符号指定
        {{ name|lower }}
    上述代码先通过 lower 过滤器调整 {{ name }} 变量的值——把文本转换成小写，然后再显示。过滤器可以串
    接，即把一个过滤器的输出传给下一个过滤器。
    下述示例获取列表中的第一个元素，然后将其转换成大写：
        {{ my_list|first|upper }}
    有些过滤器可以接受参数。过滤器的参数放在冒号之后，始终放在双引号内。例如：
        {{ bio|truncatewords:"30" }}
    上述示例显示 bio 变量的前 30 个词
    
    • addslashes：在反斜线、单引号和双引号前面添加一个反斜线。可用于转义字符串。例如：{{ value|addslashes }}。
    • date：根据参数中的格式字符串格式化 date 或 datetime 对象。例如：{{ pub_date|date:"F j, Y"
    }}。格式字符串在附录 E 中说明。
    • length：返回值的长度。对列表来说，返回元素的数量。对字符串来说，返回字符的数量。如果变量
    未定义，返回 0。

- 模板settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... 一些选项 ...
        },
    },
]
BACKEND 的值是一个点分 Python 路径，指向实现 Django 模板后端 API 的模板引擎类。内置的后端有 django.template.backends.django.DjangoTemplates 和 django.template.backends.jinja2.Jinja2。
因为多数引擎从文件中加载模板，所以各个引擎的顶层配置包含三个通用的设置：
• DIRS 定义一个目录列表，模板引擎按顺序在里面查找模板源文件。
• APP_DIRS 设定是否在安装的应用中查找模板。按约定，APPS_DIRS 设为 True 时，DjangoTemplates 会在
INSTALLED_APPS 中的各个应用里查找名为“templates”的子目录。这样，即使 DIRS 为空，模板引擎还能
查找应用模板。
• OPTIONS 是一些针对后端的设置。

• 如果不是构建没有应用的极简程序，最好留空 DIRS。设置文件默认把 APP_DIRS 设为 True，因此最好
在 Django 应用中放一个“templates”子目录。
• 如果想在项目根目录中放一些主模板（例如在 mysite/templates 目录中），需要像这样设定 DIRS：
'DIRS': [os.path.join(BASE_DIR, 'templates')],
• 模板目录不一定非得叫 'templates'，Django 不限制你用什么名称，但是坚守约定易于理解项目的结
构。如果不想遵守这个约定，或者出于某些原因不能这么做，可以指定任何目录，只要启动 Web 服务
器的用户有权读取那个目录中的模板就行。
注: 在 Windows 中要加上盘符，而且要使用 Unix 风格的正斜线，而不是反斜线，如下所示：
'DIRS': ['C:/www/django/templates']

- 帮助理解机制
        from django.template.loader import get_template
        from django.template import Context
        from django.http import HttpResponse
        import datetime
        def current_datetime(request):
        now = datetime.datetime.now()
        t = get_template('current_datetime.html')
        html = t.render(Context({'current_date': now}))
        return HttpResponse(html)
 django.template.loader.get_template() 函数调用。这个函数的参数是模板的名称，找到模板在文件系统中的位置后，
 打开那个文件，编译后返回一个 Template对象。
为了找到模板在文件系统中的位置，get_template() 按下列顺序查找：
• 如果 APP_DIRS 的值是 True，而且使用 DTL，在当前应用中查找“templates”目录。
• 如果在当前应用中没找到模板，get_template() 把传给它的模板名称添加到 DIRS 中的各个目录后面，
按顺序在各个目录中查找。假如 DIRS 的第一个元素是 '/home/django/mysite/templates'，上述
get_template() 调用查找的模板是 /home/django/mysite/templates/current_datetime.html。
• 如果 get_template() 找不到指定名称对应的模板，抛出 TemplateDoesNotExist 异常。

render() 是对 get_template() 的简单包装,render() 的第一个参数是请求对象，第二个参数是模板名称，第三个单数可选，是一个字段，用于创建传给
模板的上下文。如果不指定第三个参数，render() 使用一个空字典。


内置模板标签：{% include %}。
这个标签的作用是引入另一个模板的内容。它的参数是要引入的模板的名称，可以是变量，也可以是硬编码
的字符串（放在引号里，单双引号都行）。
- 作用一样
    {% include 'nav.html' %}
    {% include "nav.html" %}
    下述示例引入 includes/nav.html 模板的内容：
    {% include 'includes/nav.html' %}
    下述示例引入的模板名称由变量 template_name 指定：
    {% include template_name %}

        # mypage.html
        <html>
        <body>
        {% include "includes/nav.html" %}
        <h1>{{ title }}</h1>
        </body>
        </html>
        # includes/nav.html
        <div id="nav">
        You are in: {{ current_section }}
        </div>
如果 {% include %} 标签的参数指定的模板不存在，Django 会做下面两件事中的一件：
• DEBUG 为 True 时，渲染 Django 错误页面，显示 TemplateDoesNotExist 异常。
• DEBUG 为 False 时，静默，那个标签的位置什么也不显示。

- 模板继承
模板继承是指创建一个基底“骨架”模板，包含网站的所有通用部分，并且定义一些“块”，让子模板覆盖。
基模板base.html
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
        <html lang="en">
        <head>
        <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
        <h1>My helpful timestamp site</h1>
        {% block content %}{% endblock %}
        {% block footer %}
        <hr>
        <p>Thanks for visiting my site.</p>
        {% endblock %}
        </body>
        </html>
子模板可以覆盖块的内容、向块中添加内容，或者原封不动
{% block %}: 它的作用很简单，告诉模板引擎，子模板可以覆盖这部分内容。
子模板 current_datetime.html : 
        {% extends "base.html" %}
        {% block title %}The current time{% endblock %}
        {% block content %}
        <p>It is now {{ current_date }}.</p>
        {% endblock %}
原理: 模板引擎加载 current_datetime.html 模板时，发现有 {% extends %} 标签，意识到这是一个
子模板，因此立即加载父模板，即这里的 base.html。
加载父模板时，模板引擎发现 base.html 中有三个 {% block %} 标签，然后使用子模板中的内容替换。因此，
将使用 {% block title %} 中定义的标题和 {% block content %} 中定义的内容。


继承经常使用下述三层结构：
1. 创建 base.html 模板，定义网站的整体外观。这个模板的内容很少变化。
2. 为网站中的各个“区域”创建 base_SECTION.html 模板（如 base_photos.html 和 base_forum.html）。这
些模板扩展 base.html，包含各区域专属的样式和设计。
3. 为各种页面创建单独的模板，例如论坛页面或相册。这些模板扩展相应的区域模板。


• 如果模板中有 {% extends %}，必须是模板中的第一个标签。否则，模板继承不起作用。
• 一般来说，基模板中的 {% block %} 标签越多越好。记住，子模板无需定义父模板中的全部块，因此
可以为一些块定义合理的默认内容，只在子模板中覆盖需要的块。钩子多总是好的。
• 如果发现要在多个模板中重复编写相同的代码，或许说明应该把那些代码移到父模板中的一个 {%
block %} 标签里。
• 如果需要从父模板中的块里获取内容，使用 {{ block.super }}，这是一个“魔法”变量，提供父模板中
渲染后的文本。向块中添加内容，而不是完全覆盖时就可以这么做。
• 在同一个模板中不能为多个 {% block %} 标签定义相同的名称。之所以有这个限制，是因为 block 标
签是双向的。即，block 标签不仅标识供填充的空位，还用于定义填充父模板中空位的内容。如果一
个模板中有两个同名的块，那么父模板就不知道使用哪个块里的内容。
• 传给 {% extends %} 的模板名称使用与 get_template() 相同的方法加载。即，模板在 DIRS 设置定义的
目录中，或者在当前 Django 应用的“templates”目录里。
• 多数情况下，{% extends %} 的参数是字符串，不过如果直到运行时才知道父模板的名称，也可以用变
量。通过这一点可以做些动态判断。


# 待续...

-----------------------------------------------------------------------
补充内容
>>> from django.template import Context, Template
>>> t = Template('My name is {{ name }}.')
>>> c = Context({'name': 'Stephane'})
>>> t.render(c)
'My name is Stephane.'

以下情况模板系统抛出 TemplateSyntaxError：
• 无效标签
• 有效标签的无效参数
• 无效过滤器
• 有效过滤器的无效参数
• 无效模板句法
• 未关闭的标签（对需要结束标签的模板标签而言）

Django 模板系统的基本用法：
编写模板字符串，
创建 Template 对象，
创建 Context 对象，
然后调用 render() 方法。

# 不好
for name in ('John', 'Julie', 'Pat'):
t = Template('Hello, {{ name }}')
print (t.render(Context({'name': name})))
# 好
t = Template('Hello, {{ name }}')
for name in ('John', 'Julie', 'Pat'):
print (t.render(Context({'name': name})))

模板系统遇到变量名中的点号时会按照下述顺序尝试查找：
• 字典查找（如 foo["bar"]）
• 属性查找（如 foo.bar）
• 方法调用（如 foo.bar()）
• 列表索引查找（如 foo[2]）

如何处理无效变量
一般来说，如果变量不存在，模板系统在变量处插入引擎的 string_if_invalid 配置选项。这个选项的默认
值为一个空字符串。例如：
>>> from django.template import Template, Context
>>> t = Template('Your name is {{ name }}.')
>>> t.render(Context())
'Your name is .'
>>> t.render(Context({'var': 'hello'}))
'Your name is .'
>>> t.render(Context({'NAME': 'hello'}))
'Your name is .'
>>> t.render(Context({'Name': 'hello'}))
'Your name is .'
这一行为比抛出异常好，因为遇到人为错误时能迅速恢复。在上述示例中，所有查找都失败，因为变量名的
大小写不对，或者名称错误。在现实中，如果因为模板中有小小的句法错误就导致网站不可访问，着实无法
让人接受。