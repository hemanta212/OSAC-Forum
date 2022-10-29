from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from datetime import datetime, date

from notification import views as notification_views

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = reversed(Post.objects.all())
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['body', 'type','is_anonymous','tag0', 'tag1']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = date.today()
        form.instance.time = datetime.now().strftime("%H:%M:%S")
        notification_views.create_post_notification(self.request, form.instance.id)
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object.id)
        return context

def create_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        body = request.POST.get('body')
        comment = Comment(user=request.user, post=post, body=body, date=date.today(), time=datetime.now().strftime("%H:%M:%S"))
        comment.save()
        post.comments += 1
        post.save()
        notification_views.create_comment_notification(request, post_id)
        return JsonResponse({'bool': True})
    return JsonResponse({'bool': False})

def upvote(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        type = request.POST.get('type')
        if type == "comment":
            notification_views.upvote_comment_notification(request, post_id)
            comment = get_object_or_404(Comment, id=post_id)
            if comment.upvotes.filter(id=request.user.id).exists():
                comment.upvotes.remove(request.user)
            else:
                comment.upvotes.add(request.user)
            if comment.downvotes.filter(id=request.user.id).exists():
                comment.downvotes.remove(request.user)
            return JsonResponse({'bool': True})
        else:
            notification_views.upvote_post_notification(request, post_id)
            post = get_object_or_404(Post, id=post_id)
            if post.upvotes.filter(id=request.user.id).exists():
                post.upvotes.remove(request.user)
            else:
                post.upvotes.add(request.user)
            if post.downvotes.filter(id=request.user.id).exists():
                post.downvotes.remove(request.user)
            return JsonResponse({'bool': True})

def downvote(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        type = request.POST.get('type')
        
        if type == "comment":
            notification_views.downvote_comment_notification(request, post_id)
            comment = get_object_or_404(Comment, id=post_id)
            if comment.downvotes.filter(id=request.user.id).exists():
                comment.downvotes.remove(request.user)
            else:
                comment.downvotes.add(request.user)
            if comment.upvotes.filter(id=request.user.id).exists():
                comment.upvotes.remove(request.user)
            return JsonResponse({'bool': True})
        else:
            notification_views.downvote_post_notification(request, post_id)
            post = get_object_or_404(Post, id=post_id)
            if post.downvotes.filter(id=request.user.id).exists():
                post.downvotes.remove(request.user)
            else:
                post.downvotes.add(request.user)
            if post.upvotes.filter(id=request.user.id).exists():
                post.upvotes.remove(request.user)
            return JsonResponse({'bool': True})


