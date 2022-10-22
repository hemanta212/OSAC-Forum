from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('post_create/',views.PostCreateView.as_view(), name='post_create'),
    path('upvote/',views.upvote, name='upvote'),
    path('downvote/',views.downvote, name='downvote'),
    path('create_comment/',views.create_comment, name='create_comment'),
    path('post/<int:pk>',views.PostDetailView.as_view(), name='detail'),
]
