# session
- [https://www.cnblogs.com/kayb/p/7256222.html]
- 在计算机中，尤其是在网络应用中，称为“会话控制”。
  Session 对象存储特定用户会话所需的属性及配置信息.
- 为了应对HTTP协议的无状态性, 保护用户敏感信息
- 属于request的一个属性
- 常用操作:
    - request.session.get(key, defaultValue) # 得到key对应的value,如果没有,返回默认值defaultValue
    - request.session.clear() # 清空session的所有值
    - request.session[key] = value # 赋值
    - request.session.flush() # 删除当前会话且清除当前会话的cookie
    - del request.session[key] # 删除key的值
# 分页
- django提供现成的分页器用来对结果进行分页
- from django.core.paginator import Paginator
# admin
- 创建超级管理员: 
    (python36) E:\Python code\python--Django\yunxifeng_session>python manage.py createsuperuser
    Username (leave blank to use 'administrator'): yunxifeng
    Email address: xiaosuiyuan@outlook.com
    Password:
    Password (again):
    Superuser created successfully.
