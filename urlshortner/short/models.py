from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    full_name = models.CharField(max_length=30,null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.IntegerField(null=False)
    def __str__(self):
        return self.user.username


class Bitly(models.Model):
    username = models.CharField(max_length=15,null=True)
    long_url = models.URLField(null=False)
    title = models.TextField(null=True)
    shortcode = models.CharField(max_length = 6,unique = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    datewise = models.TextField()

    def __str__(self):
        return self.shortcode
