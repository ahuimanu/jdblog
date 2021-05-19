from django.db import models
from django.contrib.auth import get_user_model

# used to create the one-to-one association below
User = get_user_model()

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title