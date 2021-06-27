from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.utils import timezone


# Create your views here.
def index(request):
    blog_list_four = Post.objects.all()[:4]
    latest = Post.objects.last()
    blog_post_all = Post.objects.all()
    articles = ['article1', 'article2', 'article3', 'article4']
    trendings = ['trending1', 'trending2', 'trending3', 'trending4','trending5', 'trending6', 'trending7', 'trending8']
    newses = ['News1', 'News2', 'News3', 'News4', 'News5', 'News6']
    blog_post =['blog1', 'blog2', 'blog3', 'blog4', 'blog51', 'blog61', 'blog71', 'blog81', 'blog91', 'blog101', 'blog1', 'blog111', 'blog121', 'blog131']

    return render(request, 'blog/blog_home.html', {'latest': latest, 'lastest_four': blog_list_four, 'articles': articles, 'blog_post_all': blog_post_all, 'blogs': blog_post})


def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    images = 'image'
    article_content = 'article_content'
    return render(request, 'blog/post_details.html', {'post': post})


class BlogPostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class BlogPostDetails(ListView):
    model = Post


def tools(request):
    return render(request, 'tools/base_tools.html', {})
