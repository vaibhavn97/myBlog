from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        'posts': posts
    })

def post_detail(request, pk):
    post = Post.objects.filter(pk=pk)[0]
    return render(request, 'blog/post_detail.html', {'post':post})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'desc']
    template_name = 'blog/post_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'desc']
    template_name = 'blog/post_update.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False