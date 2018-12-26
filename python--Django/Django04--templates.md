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
- 2.if标签 
    - 用法:
        {% if 条件 %}
            条件成立执行语句
        {% elif 条件 %}}
            条件成立执行语句
        {% else %}
            以上条件都不成立执行语句
        {% endif %}}
- 3.csrf标签
    - [https://www.aliyun.com/jiaocheng/436463.html?spm=5176.100033.2.7.3da91713Q2qX7b]
    - [https://www.cnblogs.com/shytong/p/5308667.html]
    - CSRF（Cross-site request forgery）跨站请求伪造  
    - 为防范CSRF攻击,在提交表单的时候,表单页面需要加上{% csrf_token %}   
# 待续...



