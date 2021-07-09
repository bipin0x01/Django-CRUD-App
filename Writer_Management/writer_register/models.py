from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class experience(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class Writers(models.Model):
    fullname = models.CharField(max_length=50)
    writer_uid = models.CharField(max_length=4)
    mobile = models.CharField(max_length=10)
    experience = models.ForeignKey(experience,on_delete=CASCADE) 