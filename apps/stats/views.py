from django.shortcuts import render
from . models import Stat

def stat(request):
    stats = Stat.objects.filter(is_active=True).order_by('order')

    context = {
        'stats': stats,
    }

    return render(request, 'pages/stats.html', context)
