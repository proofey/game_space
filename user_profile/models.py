from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    country = models.CharField(max_length=30, blank=True)
    quote = models.CharField(max_length=200, default="...", blank=True)
    image = models.ImageField(upload_to='profile_images', default='profile_images/default_profile_pic.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)


    def get_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.user

