from django.db import models
from django.contrib.auth.models import User
from main.models import Post, Comment

# Create your models here.
class Notification(models.Model):
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='by', blank=True, null=True)
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to', blank=True, null=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post', blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        string = "notification"+' '+str(self.id)
        return string

class Viewed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='notification', blank=True, null=True)
    def __str__(self):
        string = "viewed"+' '+str(self.id)
        return string