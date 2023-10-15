from django import forms
from django.contrib import admin
from django.contrib.admin import widgets
from .models import Product, Category, Category_Product, Warehouse, Order, Delivery, Supplier, ProductWarehouse


admin.site.register(Category)
admin.site.register(Category_Product)


class CategoryInline(admin.TabularInline):
    model = Category_Product
    extra = 1


class ProductForm(forms.ModelForm):
    warehouses = forms.ModelMultipleChoiceField(
        queryset=Warehouse.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Warehouses', is_stacked=False),
        required=False,
        label='Warehouses'
    )

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'price', 'quantity', 'get_warehouse_names')
    list_filter = ('categories', 'warehouses')
    inlines = [CategoryInline]
    search_fields = ('name', 'summary')
    form = ProductForm
    filter_horizontal = ('warehouses',)
    readonly_fields = ('get_warehouse_names',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        warehouses = form.cleaned_data.get('warehouses')
        if warehouses is not None:
            for warehouse in warehouses:
                ProductWarehouse.objects.update_or_create(
                    product=obj,
                    warehouse=warehouse,
                    defaults={'quantity': obj.quantity}
                )

    def get_warehouse_names(self, obj):
        return ', '.join([str(warehouse) for warehouse in obj.warehouses.all()])
    get_warehouse_names.short_description = 'Склады'


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


@admin.register(ProductWarehouse)
class ProductWarehouseAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'quantity')
    list_filter = ('warehouse',)