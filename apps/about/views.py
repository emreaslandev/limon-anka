from django.shortcuts import render
from . models import About

def about(request):
    abouts = About.objects.filter(is_active=True).order_by('order')

    context = {
        'abouts': abouts,
    }

    return render(request, 'pages/about.html', context)
