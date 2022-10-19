from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('post_create/',views.PostCreateView.as_view(), name='post_create'),
    path('upvote/',views.upvote, name='upvote'),
    path('downvote/',views.downvote, name='upvote'),
]
