from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.SET_NULL,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return str(self.author) + '.' + self.post.title

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post = self).count()

