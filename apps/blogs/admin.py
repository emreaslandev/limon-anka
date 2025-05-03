from django.contrib import admin
from .models import Blog, Category, Media

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'order', 'slug', 'created_at', 'updated_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Media)

