from django.shortcuts import render
from .models import Faq

def faq(request):
    faqs = Faq.objects.filter(is_active=True).order_by('order')

    context = {
        'faqs': faqs
    }
    
    return render(request, 'pages/faqs.html' , context)