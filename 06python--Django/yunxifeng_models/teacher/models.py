from django.db import models

# Create your models here.
class Teacher(models.Model):
    # CharFiled表示字符串
    name = models.CharField(max_length=12)
    # IntegerFiled表示整数
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
    # 魔法函数__str__:自定义返回描述信息
    def __str__(self):
        return self.name