from django.urls import path, include
from .views import (home, like, dislike,
                    add_post, update_post,
                    post_like, your_post,
                    delete_post, edit_profile,
                    user_profile, post_view,
                    delete_image,
                    )


urlpatterns = [
    path('', home, name='home'),
    path('like/<int:postid>/', like, name='like'),
    path('dislike/<int:postid>/', dislike, name='dislike'),
    path('add_post/', add_post, name='add-post'),
    path('post_like/', post_like, name='post-like'),
    path('your_post/', your_post, name='your-post'),
    path('update_post/<int:postid>/', update_post, name='update-post'),
    path('delete_post/<int:postid>/', delete_post, name='delete-post'),
    path('edit_prifile/', edit_profile, name='edit-profile'),
    path('user_profile/<int:userid>/', user_profile, name='user-profile') ,
    path('post_view/<int:postid>/', post_view, name='post-view'),
    path('delete_image', delete_image, name='delete-image'),
]
