from django.contrib import admin
from .models import Product, Variations, ReviewRating, ProductGallery
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','created_date', 'modify_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category','variation_value','is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category','variation_value','is_active')



admin.site.register(Product, ProductAdmin)
admin.site.register(Variations, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)