from django.urls import path
from . import views


urlpatterns = [
    path('<str:forum_name>/new_post/', views.new_post, name='new-post'),
    path('<str:forum_name>/post/<int:id>', views.post_details, name='post-details'),
    path('<str:forum_name>/update_post/<int:id>/', views.update_post, name='update-post'),
    path('<str:forum_name>/delete_post/<int:id>', views.delete_post, name='delete-post'),
    path('<str:forum_name>/comment_post/<int:id>', views.new_comment, name='comment-post'),
    path('<str:forum_name>/update_comment/<int:id>', views.update_comment, name='update-comment'),
    path('<str:forum_name>/delete_comment/<int:id>', views.delete_comment, name='delete-comment'),
    path('<str:forum_name>/new_reply/<int:id>', views.new_reply, name='new-reply'),
    path('<str:forum_name>/update_reply/<int:id>', views.update_reply, name='update-reply'),
    path('<str:forum_name>/delete_reply/<int:id>', views.delete_reply, name='delete-reply'),
    path('post_notification/<int:post_id>/<int:notification_id>', views.post_notification, name='post-notification'),
]