from django.conf.urls import include, url
from django.contrib import admin
from mytpl import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'yunxifeng_templates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^one/', v.one)
]
