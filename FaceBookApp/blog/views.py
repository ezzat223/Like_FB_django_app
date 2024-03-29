from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User

from django.contrib import messages

from django.views.generic import (
    ListView,   # for whole posts
    DetailView, # for a single post
    CreateView, # for creating posts
    UpdateView,
    DeleteView,
) 

# Create your views here.

def home(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)



                # whole Posts
# when used in app(urls.py) looks for template with naming convention:
# <app>/<model>_<viewtype>.html ; which is here
# blog/post_list.html
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5      # 2 posts per page ; next page(/?page=2)



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5      # 2 posts per page ; next page(/?page=2)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # to override the form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # to override the form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        messages.error(self.request, message="You are not the author!")
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        messages.error(self.request, message="You are not the author!")
        return False



def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'blog/about.html', context)