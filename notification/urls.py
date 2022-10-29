from .views import NotificationView, mark_as_viewed
from django.urls import path

urlpatterns = [
    path('', NotificationView.as_view(), name='notification'),
    path('mark_as_viewed/<int:pk>', mark_as_viewed, name='mark_as_viewed'),
]