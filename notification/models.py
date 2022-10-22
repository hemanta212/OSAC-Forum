from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='by', blank=True, null=True)
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to', blank=True, null=True)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    is_read = models.BooleanField(default=False)
    def __str__(self):
        string = "notification"+' '+str(self.id)
        return string