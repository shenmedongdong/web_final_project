from django.db import models

# Create your models here.

class Member(models.Model):
    login_id = models.CharField(max_length=255)
    login_pw = models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title