from django.db import models



class Intro(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='intro-images')

    def __str__(self):
        return self.name