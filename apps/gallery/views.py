from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Gallery

def gallery(request):
    files = Gallery.objects.filter(is_active=True).order_by('order')
    paginator = Paginator(files, 15)  # Sayfa başına 15 öğe

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'pages/gallery.html', context)
