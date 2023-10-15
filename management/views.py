from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Product, Category, Category_Product, Warehouse, Order, Delivery, Supplier
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import datetime

def index(request):
    num_products = Product.objects.all().count()
    num_categories = Category.objects.all().count()
    num_suppliers = Supplier.objects.all().count()
    num_orders = Order.objects.all().count()
    num_deliveries = Delivery.objects.all().count()
    num_warehouses = Warehouse.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={
            'num_products': num_products,
            'num_categories': num_categories,
            'num_suppliers': num_suppliers,
            'num_orders': num_orders,
            'num_deliveries': num_deliveries,
            'num_warehouses': num_warehouses,
            'num_visits': num_visits,
        },
    )


# PRODUCT
class ProductListView(ListView):
    model = Product
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'summary', 'price', 'quantity', 'warehouse_id']
    
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'summary', 'price', 'quantity', 'warehouse_id']

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products')

# CATEGORY
class CategoryListView(ListView):
    model = Category
    paginate_by = 10

class CategoryDetailView(DetailView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'summary']

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'summary']

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')

# WAREHOUSE
class WarehouseListView(ListView):
    model = Warehouse
    paginate_by = 10
    template_name = 'warehouse_list.html'
    context_object_name = 'warehouse_list'

class WarehouseDetailView(DetailView):
    model = Warehouse

class WarehouseCreateView(CreateView):
    model = Warehouse
    fields = ['name', 'address']

class WarehouseUpdateView(UpdateView):
    model = Warehouse
    fields = ['name', 'address']

class WarehouseDeleteView(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('warehouses')

# ORDER
class OrderListView(ListView):
    model = Order
    paginate_by = 10
    template_name = 'order_list.html'
    context_object_name = 'order_list'

class OrderDetailView(DetailView):
    model = Order

class OrderCreateView(CreateView):
    model = Order
    fields = ['product', 'user', 'quantity', 'status']

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['product', 'user', 'quantity', 'status']

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders')

# DELIVERY
class DeliveryListView(ListView):
    model = Delivery
    paginate_by = 10
    template_name = 'delivery_list.html'
    context_object_name = 'delivery_list'

class DeliveryDetailView(DetailView):
    model = Delivery

class DeliveryCreateView(CreateView):
    model = Delivery
    fields = ['product', 'supplier', 'quantity', 'date']

class DeliveryUpdateView(UpdateView):
    model = Delivery
    fields = ['product', 'supplier', 'quantity', 'date']

class DeliveryDeleteView(DeleteView):
    model = Delivery
    success_url = reverse_lazy('deliveries')

# SUPPLIER
class SupplierListView(ListView):
    model = Supplier
    paginate_by = 10
    template_name = 'supplier_list.html'
    context_object_name = 'supplier_list'

class SupplierDetailView(DetailView):
    model = Supplier

class SupplierCreateView(CreateView):
    model = Supplier
    fields = ['name', 'contact', 'address', 'tel']

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = ['name', 'contact', 'address', 'tel']

class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('suppliers')
