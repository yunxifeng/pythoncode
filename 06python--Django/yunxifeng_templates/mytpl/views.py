from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    return render(request, r"one.html")

def two(request):
    # 用来存放用于渲染模板的数据
    # 上下文环境
    c = dict()
    c["name1"] = "Python"
    c["name2"] = "Linux"
    return render(request, "two.html", context=c)

def three(request):
    cc = dict()
    cc["score"] = [90,76,67,44,47,32,]
    return render(request, "three.html", context=cc)

def four(request):
    ccc = dict()
    ccc["name"] = "Unix"
    return render(request, "four.html", context=ccc)

def five_get(request):
    return render(request, "five.html")
def five_post(request):
    print(request.POST)
    return render(request, "one.html")