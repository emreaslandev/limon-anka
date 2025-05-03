from django.shortcuts import render
from . models import Slider

def slider(request):
    sliders = Slider.objects.filter(is_active=True).order_by('order')

    context = {
        'sliders': sliders,
    }

    return render(request, 'pages/sliders.html', context)