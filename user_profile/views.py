from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . models import Profile
from . forms import UpdateProfileForm
from django.contrib import messages
from post.models import Comment, Post


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author=request.user.profile).order_by('-created')
    comments = Comment.objects.filter(author=request.user.profile).order_by('-created')
    return render(request, 'user_profile/profile.html', {
        'profile': profile,
        'posts': posts,
        'comments': comments
    })

@login_required
def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    update_form = UpdateProfileForm()
    if request.method == "POST" or request.method == "FILES":
        update_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Profile Updated!')
            return redirect('profile')
    else:
        update_form = UpdateProfileForm(instance=profile)
        
    return render(request, 'user_profile/update_profile.html', {
        'update_form': update_form,
        'profile': profile
    })