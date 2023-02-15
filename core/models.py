from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name=_('user'))
    bio = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('bio'))
    image = models.ImageField(default='def.png', upload_to='profile', verbose_name=_('image'))

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            with Image.open(self.image.path) as im:
                if im.width > 300 or im.height > 300:
                    output = (300, 300)
                    im.thumbnail(output)
                    im.save(self.image.path)
    
    
class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts', verbose_name=_('user'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('content'))
   
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return f'{self.user}--{self.title}--'
    

class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name=_('user'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likess', verbose_name=_('post'))

    def __str__(self):
        return f"{self.user.username}--{self.post.title}"
    
    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')