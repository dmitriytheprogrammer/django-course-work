from django.contrib import admin
from .models import Product, Category, Category_Product, Warehouse, Order, Delivery, Supplier

admin.site.register(Category)
admin.site.register(Category_Product)


class CategoryInline(admin.TabularInline):
    model = Category_Product
    extra = 1


class ProductInline(admin.TabularInline):
    model = Warehouse.products.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'price', 'quantity')
    inlines = [CategoryInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'status')
    list_filter = ('status',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('product', 'supplier', 'quantity', 'date')
    list_filter = ('date',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'address', 'tel')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = [ProductInline]
