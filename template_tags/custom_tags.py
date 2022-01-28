from django import template
from post.models import Notification
from forum.models import Forum

register = template.Library()

@register.inclusion_tag('show_notifications.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = Notification.objects.filter(to_user=request_user).exclude(user_has_seen=True).exclude(from_user=request_user).order_by('-date')
    
    return {'notifications': notifications}


@register.inclusion_tag('show_forums.html', takes_context=True)
def show_forums(context):
    forums = Forum.objects.all()

    return {'forums': forums}