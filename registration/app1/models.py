from django.db import models
class tweet(models.Model):
    uname=models.CharField(max_length=20)
    post=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.uname+" "+self.date

# Create your models here.
