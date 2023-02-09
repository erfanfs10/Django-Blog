from django.shortcuts import render, redirect
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Profile
from .forms import PostForm, ProfileForm
from django.core.paginator import Paginator


def home(request):

    q = request.GET.get('q').lower() if request.GET.get('q') is not None else ''
    
    if q == '':
        posts = Post.objects.annotate(like=Count('likess__id')).all().order_by( '-updated_time', '-created_time')
    elif q == 'new':
        posts = Post.objects.annotate(like=Count('likess__id')).all().order_by('-created_time')
    elif q == 'like':
        posts = Post.objects.annotate(like=Count('likess__id')).all().order_by('-like')
    else:
        posts = Post.objects.annotate(like=Count('likess__id')).filter( Q(title__icontains=q) | Q(user__username__icontains=q) )

    paginator = Paginator(posts, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page') if request.GET.get('page') is not None else ''
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated:

        like = Like.objects.filter(user=request.user).values_list('post_id', flat=True)
    else:        
        like = None

    return render(request, 'core/home.html', {'posts': page_obj, 'like': like})


@login_required(login_url='login')
def like(request, postid):

    post = Post.objects.get(pk=postid)
    Like.objects.create(user=request.user, post=post)

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def dislike(request, postid):

    like = Like.objects.get(post=postid, user=request.user)
    like.delete()

    return redirect(request.META.get('HTTP_REFERER'))    


@login_required(login_url='login')
def add_post(request):

    if request.method == 'POST': 
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:        
        form = PostForm()

    return render(request, 'core/add_post.html', {'form': form})


@login_required(login_url='login')
def post_like(request):

    posts = Post.objects.annotate(like=Count('likess__id')).filter(likess__user = request.user)
    
    paginator = Paginator(posts, 6) # Show 6 contacts per page.

    page_number = request.GET.get('page') if request.GET.get('page') is not None else ''
    page_obj = paginator.get_page(page_number)

    like = Like.objects.filter(user=request.user).values_list('post_id', flat=True)

    return render(request, 'core/post_like.html', {'posts': page_obj, 'like': like})


@login_required(login_url='login')
def your_post(request):

    posts = Post.objects.annotate(like=Count('likess__id')).filter(user=request.user)
    
    paginator = Paginator(posts, 6) # Show 6 contacts per page.

    page_number = request.GET.get('page') if request.GET.get('page') is not None else ''
    page_obj = paginator.get_page(page_number)

    like = Like.objects.filter(user=request.user).values_list('post_id', flat=True)

    context = {
        'posts': page_obj,
        'like': like,
        'p': paginator
    }

    return render(request, 'core/your_post.html', context=context)


@login_required(login_url='login')
def update_post(request, postid):

    post = Post.objects.get(pk=postid)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('your-post')
   
    else:
        
        form = PostForm(instance=post)

    return render(request, 'core/update_post.html', {'form': form})        


@login_required(login_url='login')
def delete_post(request, postid):

    if request.method == "POST":
        post = Post.objects.get(pk=postid)
        post.delete()
        return redirect('your-post')

    return render(request, 'core/delete_post.html') 


@login_required(login_url='login')
def edit_profile(request):
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'core/edit_profile.html', {'form': form})


def user_profile(request, userid):

    posts = Post.objects.annotate(like=Count('likess__id')).filter(user=userid)
    pro = posts.first()

    if request.user.is_authenticated:

        like = Like.objects.filter(user=request.user).values_list('post_id', flat=True)
    else:        
        like = None

    context = {
        'posts': posts,
        'like': like,
        'pro': pro
    }

    return render(request, 'core/user_profile.html', context=context)


def post_view(request, postid):

    post = Post.objects.annotate(like=Count('likess__id')).filter(pk=postid).first()

    return render(request, 'core/post.html', {'post': post})


@login_required(login_url='login')
def delete_image(request):

    Profile.objects.filter(user=request.user).update(image='def.png')

    return redirect('edit-profile')
