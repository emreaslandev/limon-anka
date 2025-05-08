from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),

    path('', include('apps.homepage.urls')),
    path('hakkimizda/', include('apps.about.urls')),
    path('brands/', include('apps.brands.urls')),
    path('blogs/', include('apps.blogs.urls')),
    path('contact/', include('apps.contact.urls')),
    path('faqs/', include('apps.faqs.urls')),
    path('features/', include('apps.features.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('home/', include('apps.homepage.urls')),
    path('products/', include('apps.products.urls')),
    path('referances/', include('apps.referances.urls')),
    path('services/', include('apps.services.urls')),
    path('sliders/', include('apps.sliders.urls')),
    path('stats/', include('apps.stats.urls')),
    path('testimonials/', include('apps.testimonials.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




admin.site.site_header = '--------------'
admin.site.site_title = '-------------- YÖNETİM PANELİ'
admin.site.index_title = '-------------- YÖNETİM PANELİNE HOŞ GELDİNİZ'