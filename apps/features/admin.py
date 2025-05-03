from django.contrib import admin
from .models import Feature

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('icon', 'order', 'is_active')


admin.site.register(Feature, FeatureAdmin)