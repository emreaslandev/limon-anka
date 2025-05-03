from django.shortcuts import render, get_object_or_404
from . models import Service

def service_list(request):

    services = Service.objects.filter(is_active=True).order_by('order')
    context = {
        'services': services
    }
    return render(request, 'pages/services.html', context)

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    services = Service.objects.all().order_by('order')

    context = {
        'service': service,
        'services': services
    }

    return render(request, 'details/service_detail.html', context)