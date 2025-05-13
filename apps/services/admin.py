# from django.contrib import admin
# from .models import Service, Media, Category

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'order')
#     list_editable = ('order',)

# class MediaInline(admin.TabularInline):
#     model = Media
#     extra = 1

# class ServiceAdmin(admin.ModelAdmin):
#     inlines = [MediaInline]
#     list_display = ('title', 'category', 'is_active', 'order', 'slug')
#     list_editable = ('order', 'is_active')

# admin.site.register(Service, ServiceAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Media)