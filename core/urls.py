from django.urls import path
from .views import (like, dislike,
                    user_profile, post_view,
                    delete_image, Search, PostUpdate, PostDelete, MyPost, Home,
                    PostLike, PostAdd, ProfileUpdate
                    )


urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('like/<int:postid>/', like, name='like'),
    path('dislike/<int:postid>/', dislike, name='dislike'),
    path('add_post/', PostAdd.as_view(), name='add-post'),
    path('post_like/', PostLike.as_view(), name='post-like'),
    path('your_post/', MyPost.as_view(), name='your-post'),
    path('update_post/<int:pk>/', PostUpdate.as_view(), name='update-post'),
    path('delete_post/<int:pk>/', PostDelete.as_view(), name='delete-post'),
    path('edit_prifile/', ProfileUpdate.as_view(), name='edit-profile'),
    path('user_profile/<int:userid>/', user_profile, name='user-profile') ,
    path('post_view/<int:postid>/', post_view, name='post-view'),
    path('delete_image', delete_image, name='delete-image'),
    
]
