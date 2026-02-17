from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=127)
    content = models.CharField(max_length=127)
