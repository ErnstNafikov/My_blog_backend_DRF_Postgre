from django.db import models

class InfoBlog(models.Model):
    title = models.CharField(max_length=1000)
    info = models.CharField(max_length=4000)
