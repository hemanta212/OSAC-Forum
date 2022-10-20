from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from datetime import datetime, date

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['user', 'body', 'type', 'tag0', 'tag1']
    success_url = '/'

    def form_valid(self, form):
        #form.instance.user = self.request.user
        form.instance.date = date.today()
        form.instance.time = datetime.now().strftime("%H:%M:%S")
        return super().form_valid(form)

def upvote(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
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
        post = get_object_or_404(Post, id=post_id)
        if post.downvotes.filter(id=request.user.id).exists():
            post.downvotes.remove(request.user)
        else:
            post.downvotes.add(request.user)
        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        return JsonResponse({'bool': True})
