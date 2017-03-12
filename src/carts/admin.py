from django.contrib import admin

import models

# Register your models here.
class CartItemInline(admin.TabularInline):
    model = models.CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemInline,)
    class Meta:
        model = models.Cart


admin.site.register(models.Cart, CartAdmin)