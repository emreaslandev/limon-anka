from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_phone')
    
    # def has_add_permission(self, request):
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False
