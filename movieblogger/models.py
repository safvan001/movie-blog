from django.db import models
class movie(models.Model):
    img=models.ImageField(upload_to='movieblog/img',null=True,blank=True)
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=200)

# Create your models here.
