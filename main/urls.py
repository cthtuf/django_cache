from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

from .views import (redis, memory, model_cached, template_fragment)


urlpatterns = [
    url(r'^$', cache_page(10)(
        TemplateView.as_view(template_name='main.html')),
        name='main'),
    url(r'^simple/$', cache_page(10)(
        TemplateView.as_view(template_name='simple.html')),
        name='simple'),
    url(r'^redis/$', redis, name='redis'),
    url(r'^memory/$', memory, name='memory'),
    url(r'^model_cached/$', model_cached, name='model_cached'),
    url(r'^template_fragment/$', template_fragment, name='template_fragment'),
]