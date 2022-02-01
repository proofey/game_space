from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from . models import Notification, Post, Forum, Categories, Comment, Reply
from . forms import PostForm, PostUpdateForm, CommentForm, CommentUpdateForm, ReplyForm, ReplyUpdateForm
from django.contrib import messages


@login_required
def new_post(request, forum_name):
    categories = Categories.objects.filter(forum__name=forum_name)
    forum = get_object_or_404(Forum, name=forum_name)

    if request.method == "POST":
        form = PostForm(request.POST)
        form.fields['categories'].queryset = categories
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user.profile
            obj.forum = forum
            obj.save()
            form.save_m2m()
            messages.success(request, 'Post successful!')
            return redirect(reverse('forum-page', args=(forum_name,)))
    else:
        form = PostForm()
        form.fields['categories'].queryset = categories

    return render(request, 'post/new_post.html', {
        'form': form,
        'forum': forum
    })

@login_required
def post_details(request, forum_name, id):
    post = Post.objects.get(pk=id)
    categories = post.categories.all
    comments = Comment.objects.filter(post=post)
    forum = get_object_or_404(Forum, name=forum_name)
    
    return render(request, 'post/post_details.html', {
        'post': post,
        'categories': categories,
        'comments': comments,
        'forum': forum
    })

@login_required
def update_post(request, forum_name,id):
    post = Post.objects.get(id=id)   
    categories = Categories.objects.filter(forum__name=forum_name)
    forum = get_object_or_404(Forum, name=forum_name)
    comments = Comment.objects.filter(post=post)
    
    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        form.fields['categories'].queryset = categories
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user.profile
            obj.forum = forum
            obj.save()
            form.save_m2m()
            messages.success(request, 'Post updated!')
            return redirect(reverse('post-details', args=(forum_name, id,)))
    else:
        form = PostUpdateForm(instance=post)
        form.fields['categories'].queryset = categories
   
    return render(request, 'post/update_post.html', {
        'form': form,
        'post': post,
        'forum': forum,
        'comments': comments,
    })

@login_required
def delete_post(request, forum_name, id):
    post = Post.objects.get(id=id)
    user = request.user
    forum = get_object_or_404(Forum, name=forum_name)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST" and user.is_authenticated:
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect(reverse('forum-page', args=(forum_name,)))
    
    return render(request, 'post/delete_post.html', {
        'post': post,
        'forum': forum,
        'comments': comments,
    })

@login_required
def new_comment(request, forum_name, id):
    post = Post.objects.get(id=id)
    forum = get_object_or_404(Forum, name=forum_name)
    comments = Comment.objects.filter(post=post)
    posts = Post.objects.filter(forum__name=forum_name).order_by('-created')
    categories = Categories.objects.filter(forum__name=forum_name)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.author = request.user.profile
            obj.save()

            if request.user != post.author.user:
                notification = Notification.objects.create(notification_type=2, to_user=post.author.user, from_user=request.user , post=post)

            messages.success(request, "You successfuly posted a comment")
            return redirect(reverse('post-details', args=(forum_name, id,)))
    else:
        form = CommentForm()

    return render(request, 'post/comment_post.html', {
        'form': form,
        'post': post,
        'forum': forum,
        'comments': comments,
        'posts': posts,
        'categories': categories,
    })

@login_required  
def update_comment(request, forum_name, id):
    comment = Comment.objects.get(id=id)
    post = Post.objects.get(comment=comment)
    forum = get_object_or_404(Forum, name=forum_name)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        form = CommentUpdateForm(request.POST, instance=comment)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user.profile
            obj.post = post
            obj.save()
            messages.success(request, 'Comment updated!')
            return redirect(reverse('post-details', args=(forum_name, post.pk,)))
    else:
        form = CommentUpdateForm(instance=comment)
    
    return render(request, 'post/update_comment.html', {
        'form': form,
        'post': post,
        'forum': forum,
        'comments': comments,
    })

@login_required
def delete_comment(request, forum_name, id):
    comment = Comment.objects.get(id=id)
    post = Post.objects.get(comment=comment)
    forum = get_object_or_404(Forum, name=forum_name)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST" and request.user.is_authenticated:
        comment.delete()
        messages.success(request, 'Comment deleted!')
        return redirect(reverse('post-details', args=(forum_name, post.pk,)))
    
    return render(request, 'post/delete_comment.html', {
        'post': post,
        'forum': forum,
        'comments': comments,
    })

@login_required
def new_reply(request, forum_name, id):
    comment = Comment.objects.get(id=id)
    post = Post.objects.get(comment=comment)
    forum = get_object_or_404(Forum, name=forum_name)
    comments = Comment.objects.filter(post=post)
    
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.comment = comment
            obj.author = request.user.profile
            obj.save()

            if request.user != comment.author.user:
                notification = Notification.objects.create(notification_type=2, to_user=comment.author.user, from_user=request.user, comment=comment)

            messages.success(request, "You successfuly posted a reply")
            return redirect(reverse('post-details', args=(forum_name, post.pk,)))
    else:
        form = ReplyForm()

    return render(request, 'post/new_reply.html', {
        'form': form,
        'post': post,
        'forum': forum,
        'comments': comments,
    })

@login_required
def update_reply(request, forum_name, id):
    reply = Reply.objects.get(id=id)
    comment = Comment.objects.get(reply=reply)
    post = Post.objects.get(comment=comment)
    forum = get_object_or_404(Forum, name=forum_name)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        form = ReplyUpdateForm(request.POST, instance=reply)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.comment = comment
            obj.author = request.user.profile
            obj.save()
            messages.success(request, "Reply updated!")
            return redirect(reverse('post-details', args=(forum_name, post.pk,)))
    
    else:
        form = ReplyUpdateForm(instance=reply)

    return render(request, 'post/update_reply.html', {
        'form': form,
        'post': post,
        'forum': forum,
        'comments': comments,
    })

@login_required
def delete_reply(request, forum_name, id):
    reply = Reply.objects.get(id=id)
    post = Post.objects.get(comment__reply=reply)
    forum = get_object_or_404(Forum, name=forum_name)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST" and request.user.is_authenticated:
        reply.delete()
        messages.success(request, "Reply deleted!")
        return redirect(reverse('post-details', args=(forum_name, post.pk,)))

    return render(request, 'post/delete_reply.html', {
        'post': post,
        'forum': forum,
        'comments': comments,
    })

@login_required
def post_notification(request, post_id, notification_id):
    post = Post.objects.get(id=post_id)
    notification = Notification.objects.get(id=notification_id)
    forum_name = post.forum.name

    notification.user_has_seen = True
    notification.save()

    return redirect(reverse('post-details', args=(forum_name, post_id,)))