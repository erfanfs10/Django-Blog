from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='def.png', upload_to='profile')

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def save(self):
        super().save()
        with Image.open(self.image.path) as im:
            if im.width > 300 or im.height > 300:
                output = (300, 300)
                im.thumbnail(output)
                im.save(self.image.path)
   
   
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
    
    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')