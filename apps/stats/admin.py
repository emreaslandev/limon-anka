from django.contrib import admin
from .models import Stat

class StatAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'order', 'is_active')
    list_editable = ('value', 'order', 'is_active')

admin.site.register(Stat, StatAdmin)


