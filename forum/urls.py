from django.urls import path
from . import views

urlpatterns = [
    path('<str:forum_name>/', views.forum, name='forum-page'),
    path('<str:forum_name>/<categorie>', views.single_categorie, name='single-categorie'),
    path('<str:forum_name>/top_posts/', views.top_posts, name='top-posts')
]