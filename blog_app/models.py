from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.TextField(null=True, default='author')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
