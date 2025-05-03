from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('file', 'type', 'order', 'is_active')
    list_editable = ('order', 'is_active')

admin.site.register(Gallery, GalleryAdmin)