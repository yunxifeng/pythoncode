from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import defaults
from django.template import loader
# Create your views here.

# request参数包含传入请求相关的所有内容
def teacher(request):
    return HttpResponse("这是teacher的一个视图函数")
def do_exp(request):
    # 引发异常
    # 若要返回标准404页面,需要将主settings里DEBUG的值改为False,将ALLOWED_HOSTS改为任意"*"
    raise Http404


# 重定向
def v10_1(request):
    # 重定向到v11
    return HttpResponseRedirect("/v11")

def v10_2(request):
    # 这里用了reverse,目的在于当url->v11改变名称时,此处不用更改
    return HttpResponseRedirect(reverse("v11"))

def v11(request):
    return HttpResponse("哈哈，这是v11的访问返回呀")

# GET
def v8_get(request):
    rst = ""
    for k,v in request.GET.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("Get value of Requestion is {0}".format(rst))

# POST
def v9_get(request):
    # 渲染模板并返回
    return render_to_response("for_post.html")
def v9_post(request):
    rst = ""
    # 这里的hobby如果是多选,会默认选择最后一个
    for k,v in request.POST.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("Get value of POST is {0}".format(rst))

# 手动编写views-01
def render1_test(request):
    # 环境变量
    c = dict()

    rsp = render(request,"render1.html")
    # 等同于 rsp = HttpResponse(request, "render1.html")
    print(type(rsp))
    return rsp

# 手动编写views-02
def render2_test(request):
    # 环境变量: 把数值传进模板
    c = dict()
    # 给name变量赋值
    c["name"] = "yunxifeng"

    # context=上下文环境
    rsp = render(request, "render2.html", context=c)
    return rsp

# 手动编写views-03
def render3_test(request):
    from django.template import loader
    # 得到模板,需要导入loader
    # 手动装载模板,返回template实例
    t = loader.get_template("render3.html")
    # 类型:Template
    print(type(t))

    # {}:设置上下文环境
    # 渲染模板
    r = t.render({"name":"death"})
    # 注: 此处r的类型是:SafeText
    print(type(r))

    # 必须返回Response的子类
    return HttpResponse(r)

# render_to_response
def render4_test(request):
    rsp = render_to_response("render4.html", context={"name":"madao"})
    print(type(rsp))
    # render_to_response返回HttpResponse类型
    return rsp

# 系统内建视图
def get404(request):
    # 需要导入defaults
    return defaults.page_not_found(request, Exception)