from django.db import models
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse
from post.utils import time_difference
from django.utils import timezone
from forum.models import Forum

 


class Categories(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single-categorie', args=(self.forum, self.name,))


class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories, related_name='categories')
    topic = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.topic} -- {self.author} -- {self.created}"

    def get_absolute_url(self):
        return reverse('post-details', args=(self.forum, self.pk,))

    def show_updated(self):
        difference = time_difference(self)
        return difference

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comment')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.post}"

    def show_updated(self):
        difference = time_difference(self)
        return difference


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.comment}"

    def show_updated(self):
        difference = time_difference(self)
        return difference

class Notification(models.Model):
    # notification types:
    # 1 = like, 2 = comment
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_to', null=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_from', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    user_has_seen = models.BooleanField(default=False)
