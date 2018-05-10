from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views


urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^explore_data$', hello.views.explore_data, name='explore_data'),
    path('admin/', admin.site.urls),
]
