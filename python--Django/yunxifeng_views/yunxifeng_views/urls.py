from django.conf.urls import include, url
from django.contrib import admin
from teacher_app import views as v
urlpatterns = [
    # Examples:
    # url(r'^$', 'yunxifeng_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^teacher/', v.teacher),
    url(r'^exp/', v.do_exp),

    # 重定向
    url(r'^v10_1/', v.v10_1),
    url(r'^v10_2/', v.v10_2),
    url(r'^v11_hello/', v.v11, name="v11"),

    # GET
    # e.g. http://127.0.0.1:8000/v8/?name=yunxifeng&age=21&sex=man
    url(r'^v8/', v.v8_get),

    # POST
    url(r'^v9_get', v.v9_get),
    url(r'^v9_post', v.v9_post),

    # 手动编写views
    # render
    url(r'^render1_test', v.render1_test),
    url(r'^render2_test', v.render2_test),
    url(r'^render3_test', v.render3_test),
    # render_to_response
    url(r'^render4_test', v.render4_test),

    # 系统内建视图
    url(r'^get404', v.get404),
]
