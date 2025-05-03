from django.contrib import admin
from .models import Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')

admin.site.register(Slider, SliderAdmin)


