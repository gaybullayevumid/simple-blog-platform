from django.shortcuts import render
from .models import Post

# Create your views here.

def getPosts(request):
    template_name = 'pages/blog.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request=request, template_name=template_name, context=context)

# def post_detail(request, pk):
#     template_name = 'pages/blog_detail.html'
#     post = Post.objects.get(pk=pk)
#     last_posts = Post.objects.order_by('-created_on')
#     context = {
#                 'post': post,
#                 'last_posts':last_posts
#                }
#     return render(request=request, template_name=template_name, context=context)