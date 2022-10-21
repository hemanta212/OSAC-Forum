from django.db import models
from django.contrib.auth.models import User
# Create your models here.

post_type = (('Help','Help'),
            ('Discussion','Discussion'),
            ('Announcement','Announcement'),
            ('Rant','Rant'),
            ('Casual','Casual'),
            ('Other','Other'))

tag_choice = (('General','General'),
            ('Academics','Academics'),
            ('Career','Career'),
            ('Health','Health'),
            )  #have to add more interesting ones


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    upvotes = models.ManyToManyField(User, related_name='upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvotes', blank=True)
    comments = models.IntegerField(default=0)
    is_anonymous = models.BooleanField(default=False)
    type = models.CharField(max_length=12, choices=post_type)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    tag0 = models.CharField(max_length=100, choices= tag_choice, blank=True, null=True)
    tag1 = models.CharField(max_length=100, choices= tag_choice, blank=True, null=True)

    def __str__(self):
        string = str(self.id)+": "+ str(self.user)
        return string
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='comment_downvotes', blank=True)
    
    def __str__(self):
        string = "comment"+' '+str(self.id)+": "+str(self.user)
        return string