from django.contrib import admin
from . models import Post, Categories, Forum, Comment, Reply, Notification

admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Notification)
