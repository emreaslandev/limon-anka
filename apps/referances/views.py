from django.shortcuts import render, get_object_or_404
from . models import Referance

def referance_list(request):

    referances = Referance.objects.filter(is_active=True).order_by('order')
    context = {
        'referances': referances
    }
    return render(request, 'pages/referances.html', context)

def referance_detail(request, slug):
    referance = get_object_or_404(Referance, slug=slug)
    referances = Referance.objects.all().order_by('order')

    context = {
        'referance': referance,
        'referances': referances
    }

    return render(request, 'details/referance_detail.html', context)