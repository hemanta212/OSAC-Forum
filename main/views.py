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

    def has_upvoted(self, post):
        return post.upvotes.filter(id=self.request.user.id).exists()
    def has_downvoted(self, post):
        return post.downvotes.filter(id=self.request.user.id).exists()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['has_upvoted'] = self.has_upvoted
        context['has_downvoted'] = self.has_downvoted
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
    print('upvote')
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)
        print(post.votes())
        
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
