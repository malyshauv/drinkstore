from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_html_photo', 'price', 'is_enabled')
    list_editable = ('price', 'is_enabled')
    list_filter = ('category', 'is_enabled')
    search_fields = ('name', 'description')
    def get_html_photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")
        return "Нет фото"
    get_html_photo.short_description = "Миниатюра"    
