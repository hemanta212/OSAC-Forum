from django import template
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