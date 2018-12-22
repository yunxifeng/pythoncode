from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# request参数包含请求相关的所有内容
def teacher(request):
    return HttpResponse("这是teacher的一个视图函数")