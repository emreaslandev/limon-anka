from django.shortcuts import render
from apps.about.models import About
from apps.blogs.models import Blog
# from apps.brands.models import Brand
# from apps.contact.models import Contact
from apps.faqs.models import Faq
from apps.features.models import Feature
from apps.gallery.models import Gallery
from apps.products.models import Product
# from apps.referances.models import Referance
# from apps.services.models import Service
from apps.sliders.models import Slider
from apps.stats.models import Stat
from apps.testimonials.models import Testimonial

def home(request):
    about = About.objects.filter(is_active=True).first()
    blogs = Blog.objects.filter(is_active=True).order_by('order')[:3]
    # brands = Brand.objects.filter(is_active=True).order_by('order')
    # contacts = Contact.objects.filter(is_active=True).first()
    faqs = Faq.objects.filter(is_active=True).order_by('order')[:6]
    features = Feature.objects.filter(is_active=True).order_by('order')[:6]
    gallery = Gallery.objects.filter(is_active=True).order_by('order')[:6]
    products = Product.objects.filter(is_active=True).order_by('order')[:6]
    # referances = Referance.objects.filter(is_active=True).order_by('order')[:6]
    # services = Service.objects.filter(is_active=True).order_by('order')[:6]
    sliders = Slider.objects.filter(is_active=True).order_by('order')
    stats = Stat.objects.filter(is_active=True).order_by('order')
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order')
    context = {
        'about': about,
        'blogs': blogs,
        # 'brands': brands, 
        # 'contacts': contacts,
        'faqs': faqs,
        'features': features,
        'gallery': gallery,
        'products': products,
        # 'referances': referances,
        # 'services': services,
        'sliders': sliders,
        'stats': stats,
        'testimonials': testimonials,
    }
    return render(request, 'pages/index.html', context)
