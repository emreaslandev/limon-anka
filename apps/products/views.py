from django.shortcuts import render, get_object_or_404
from . models import Product

def product_list(request):

    products = Product.objects.filter(is_active=True).order_by('order')
    context = {
        'products': products
    }
    return render(request, 'pages/products.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    products = Product.objects.all().order_by('order')

    context = {
        'product': product,
        'products': products
    }

    return render(request, 'details/product_detail.html', context)