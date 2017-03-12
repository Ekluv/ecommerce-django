from django.contrib import admin

import models


class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = (VariationInline, ProductImageInline)
    list_display = ('__unicode__', 'price')
    class Meta:
        model = models.Product



# Register your models here.
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)
admin.site.register(models.ProductFeatured)