from django.db import models

# Create your models here.
class blogPost(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    owner_name = models.CharField(max_length=25)
    