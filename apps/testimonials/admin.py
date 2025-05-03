from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'type', 'role', 'order', 'is_active')
    list_editable = ('order', 'is_active')

admin.site.register(Testimonial, TestimonialAdmin)


