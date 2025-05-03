from django.contrib import admin
from .models import About
from django.contrib.auth.models import User, Group

# User ve Group modellerini kayıttan çıkar
admin.site.unregister(User)
admin.site.unregister(Group)
 
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','order','is_active')
    list_editable = ('order', 'is_active')

admin.site.register(About, AboutAdmin)