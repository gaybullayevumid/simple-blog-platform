from django.shortcuts import render
from .models import Post

# Create your views here.

def getPosts(request):
    template_name = 'pages/blog.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request=request, template_name=template_name, context=context)