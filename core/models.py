from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='def.png', upload_to='profile')

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()
   
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user}--{self.title}--'
    

class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likess')

    def __str__(self):
        return f"{self.user.username}--{self.post.title}"
    