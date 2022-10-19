from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Vote, Comment

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    context_object_name= 'posts'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['user', 'body', 'type', 'tag0', 'tag1']
