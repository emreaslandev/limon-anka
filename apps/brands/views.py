from django.shortcuts import render
from .models import Brand

def brand(request):
    brands = Brand.objects.filter(is_active=True).order_by('order')

    context = {
        'brands': brands
    }
    
    return render(request, 'pages/brands.html' , context)