from django.shortcuts import render
from . models import Feature

def feature(request):
    features = Feature.objects.filter(is_active=True).order_by('order')

    context = {
        'features': features,
    }

    return render(request, 'pages/features.html', context)
