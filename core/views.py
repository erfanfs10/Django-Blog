from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, UpdateView, ListView, CreateView
from django.views import View
from core.models import Post, Like, Profile
from core.forms import PostForm, ProfileForm


class Home(ListView):
    template_name = "core/home.html"
    paginate_by = 6
    context_object_name = "posts"

    def get_queryset(self):
        q = self.request.GET.get("q", "-created_time").lower()
        posts = Post.objects.select_related('user__profile').annotate(like=Count('likess__id')).order_by(q)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            like = Like.objects.filter(user=self.request.user).values_list('post_id', flat=True)
        else:
            like = None
        context["like"] = like
        return context    


class Search(ListView):
    template_name = "core/search.html"
    paginate_by = 6
    context_object_name = "posts"

    def get_queryset(self):
        q = self.request.GET.get("q", "")
        posts = Post.objects.select_related('user__profile').annotate(like=Count('likess__id')).filter(
            Q(title__icontains=q) | Q(user__username__icontains=q) ).order_by("-created_time")        
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            like = Like.objects.filter(user=self.request.user).values_list('post_id', flat=True)
        else:
            like = None
        context["like"] = like
        return context    


@login_required()
def like(request, postid):
    try: 
         post = Post.objects.get(pk=postid)
    except: 
        return Http404    
   
    Like.objects.create(user=request.user, post=post)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required()
def dislike(request, postid):
    try:
        like = Like.objects.get(post=postid, user=request.user)
    except:
        return Http404

    like.delete()
    return redirect(request.META.get('HTTP_REFERER'))    


class PostAdd(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "core/add_post.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class PostLike(LoginRequiredMixin, ListView):
    paginate_by = 6
    context_object_name = "posts"
    template_name = "core/post_like.html"

    def get_queryset(self):
        posts = Post.objects.select_related('user__profile').prefetch_related('likess').annotate(like=Count('likess__id')).filter(
            likess__user = self.request.user)
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like = Like.objects.filter(user=self.request.user).values_list('post_id', flat=True)
        context["like"] = like
        return context


class ProfileUpdate(LoginRequiredMixin, View):
    form_class = ProfileForm

    def get(self, request):
        form = self.form_class(instance=request.user.profile)
        return render(request, 'core/edit_profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request, 'core/edit_profile.html', {'form': form})


class ProfileUser(ListView):
    template_name = 'core/user_profile.html'
    paginate_by = 6
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.select_related('user__profile').annotate(like=Count('likess__id')).filter(
            user=self.kwargs['pk']).order_by("-created_time")
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            like = Like.objects.filter(user=self.request.user).values_list('post_id', flat=True)
        else:
            like = None
        context["like"] = like
        return context    


class PostDetail(View):
    
    def get(self, request, pk):
        post = Post.objects.annotate(like=Count('likess__id')).filter(pk=pk).first()

        if request.user.is_authenticated:
            like = Like.objects.filter(user=request.user, post=pk)
        else:        
            like = None
        return render(request, 'core/post.html', {'post': post, 'like':like})


@login_required()
def delete_image(request):

    Profile.objects.filter(user=request.user).update(image='def.png')

    return redirect('edit-profile')


class MyPost(LoginRequiredMixin, ListView):
    paginate_by = 6
    template_name = "core/your_post.html"
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.select_related('user__profile').prefetch_related('likess').annotate(like=Count('likess__id')).filter(
            user=self.request.user).order_by("-created_time")
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like = Like.objects.filter(user=self.request.user).values_list('post_id', flat=True)
        context["like"] = like
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ("title", "body")
    template_name = "core/update_post.html"
    success_url = reverse_lazy("your-post")


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "core/delete_post.html"
    success_url = reverse_lazy("your-post")
    