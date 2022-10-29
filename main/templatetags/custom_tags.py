from django import template
from notification.models import Notification, Viewed
register = template.Library()


@register.simple_tag
def has_upvoted(post, user):
    if post.upvotes.filter(id=user.id).exists():
        return "Upvoted"
    return "Upvote"

@register.simple_tag
def has_downvoted(post, user):
    if post.downvotes.filter(id=user.id).exists():
        return "Downvoted"
    return "Downvote"

@register.simple_tag
def votes(post):
    return post.upvotes.count() - post.downvotes.count()

@register.simple_tag
def has_viewed(notification, user):
    if notification.viewed.filter(user=user).exists():
        return '#00FF00'
    return '#FFFFFF'

@register.simple_tag
def no_of_notifications(user):
    count = Viewed.objects.filter(user=user).count()
    return Notification.objects.filter(to=user).count() - count  