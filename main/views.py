import random
import time

from django.template.response import TemplateResponse
from django.views.decorators.cache import cache_page

from .models import CachedByCacheOps


def get_random_list(length=10):
    return [random.randint(0, 1000) for r in range(length)]


@cache_page(10, cache='redis')
def redis(request):
    return TemplateResponse(request, 'redis.html',
                            {'items': get_random_list()})


@cache_page(10, cache='memory')
def memory(request):
    return TemplateResponse(request, 'memory.html',
                            {'items': get_random_list()})


def template_fragment(request):
    return TemplateResponse(request, 'template_fragment.html',
                            {'items': get_random_list()})


def model_cached(request):
    # Dummy loading data to DB. Factories will be in the example
    # of test features
    if CachedByCacheOps.objects.count() == 0:
        for r in range(10):
            CachedByCacheOps(data=str(random.randint(0, 1000))).save()
    return TemplateResponse(request, 'model_cached.html',
                            {'items': CachedByCacheOps.objects.all()})
