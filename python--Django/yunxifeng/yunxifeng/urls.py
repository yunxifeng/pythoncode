from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacherurls
urlpatterns = [
    # Examples:
    # url(r'^$', 'yunxifeng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # 约定,凡是由teacher模块处理的views的url都以teacher开头
    url(r'^teacher/', include(teacherurls)),

    # views函数只有名称,没有参数和括号
    url(r'^normalmap/', tv.do_normalmap),
    # 尖号表示以后面内容开头的表达式
    # 圆括号表示的是一个参数,里面的内容作为参数传递给被调用的函数
    # 参数名称以"?+P(大写)"开头,尖括号里面是参数的名称
    # 尖括号后面表示正则,[0-9]表示内容只能由是0-9的数字构成,{4}前面内容出现的次数
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])', tv.withparam),

    url(r'^book/(?:page-(?P<page_number>\d+)/)$', tv.do_book),

    url(r'^yourname/$', tv.extremParam, {"name":"yunxifeng"}),

    url(r'^myname/$', tv.revParse, name="askname"),
]
