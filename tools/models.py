
from django.db import models


class Tools(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.JSONField()

    