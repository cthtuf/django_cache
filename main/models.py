from django.db import models


class CachedByCacheOps(models.Model):
    data = models.CharField(max_length=255)
