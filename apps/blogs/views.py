from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.filter(is_active=True).order_by('order')
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/blogs.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'details/blog_detail.html', context)