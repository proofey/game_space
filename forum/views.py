from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from post.models import Post, Categories
from django.db.models import Count
from . models import Forum


@login_required
def forum(request, forum_name):
    posts = Post.objects.filter(forum__name=forum_name).order_by('-created')
    categories = Categories.objects.filter(forum__name=forum_name)
    forum = get_object_or_404(Forum, name=forum_name)

    return render(request, 'forum/forum.html', {
        'posts': posts,
        'categories': categories,
        'forum': forum
    })

@login_required
def top_posts(request, forum_name):
    posts = Post.objects.annotate(num_comments=Count('comment')).order_by('-num_comments').filter(forum__name=forum_name)
    categories = Categories.objects.filter(forum__name=forum_name)
    forum = get_object_or_404(Forum, name=forum_name)

    return render(request, 'forum/forum.html', {
        'posts': posts,
        'categories': categories,
        'forum': forum
    })

@login_required
def single_categorie(request, forum_name, categorie):
    posts = Post.objects.filter(categories__name=categorie).order_by('-created')
    categories = Categories.objects.filter(forum__name=forum_name)
    forum = get_object_or_404(Forum, name=forum_name)

    return render(request, 'forum/forum.html', {
        'posts': posts,
        'categories': categories,
        'forum': forum
    })

