from django.shortcuts import render
from . models import Testimonial

def testimonial(request):
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order')

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'pages/testimonials.html', context)
