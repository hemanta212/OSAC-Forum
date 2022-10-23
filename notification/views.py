from django.shortcuts import render
from django.db.models.signals import post_save
from .models import Notification
from main.models import Post, Comment
from django.shortcuts import render, redirect
from django.dispatch import receiver
from django.views.generic import ListView
from notification.models import Notification
from django.shortcuts import get_object_or_404
from datetime import date, datetime
# Create your views here.

#all the functions can probaly be made as methods of a class


def create_post_notification(request, post_id):
    by = request.user
    post = get_object_or_404(Post, id=post_id)
    #to = instance.user
    body =  by.username+" has created a post"
    Notification(by=by, to=None, body=body, date=date.today(), time=datetime.now()).save()

def create_comment_notification(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = get_object_or_404(Post, id=comment.post.id)
    by = request.user
    to = post.user
    body =  by.username+" has commented on your post"
    Notification(by=by, to=to, body=body, date=date.today(), time=datetime.now()).save()

def upvote_comment_notification(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = get_object_or_404(Post, id=comment.post.id)
    body = request.user.username+" has upvoted your comment"
    Notification(by=request.user, to=post.user, body=body, date=date.today(), time=datetime.now().strftime("%H:%M:%S")).save()

def downvote_comment_notification(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = get_object_or_404(Post, id=comment.post.id)
    body = request.user.username+" has downvoted your comment"
    Notification(by=request.user, to=post.user, body=body, date=date.today(), time=datetime.now().strftime("%H:%M:%S")).save()

def upvote_post_notification(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    body = request.user.username+" has upvoted your post"
    Notification(by=request.user, to=post.user, body=body, date=date.today(), time=datetime.now().strftime("%H:%M:%S")).save()

def downvote_post_notification(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    body = request.user.username+" has downvoted your post"
    Notification(by=request.user, to=post.user, body=body, date=date.today(), time=datetime.now().strftime("%H:%M:%S")).save()


class NotificationView(ListView):
    model = Notification
    template_name = 'notification.html'
    ordering = ['-date', '-time']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = reversed(Notification.objects.filter(to=None))
        print(context['notifications'])
        context['specific_notifications'] = reversed(Notification.objects.filter(to=self.request.user))
        return context

