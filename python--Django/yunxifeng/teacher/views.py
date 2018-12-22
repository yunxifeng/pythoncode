from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
'''
views函数需要一个HttpResponse类型的参数
'''
def do_normalmap(request):
    return HttpResponse("This is normalmap.")