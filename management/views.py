from django.views import generic
from django.shortcuts import render
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
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={'num_products': num_products, 
                 'num_categories': num_categories,
                 'num_visits': num_visits},
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
    permission_required = 'management.can_mark_returned'
    
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'summary', 'price', 'quantity', 'warehouse_id']
    permission_required = 'management.can_mark_returned'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products')
    permission_required = 'management.can_mark_returned'

# CATEGORY
class CategoryListView(ListView):
    model = Category
    paginate_by = 10

class CategoryDetailView(DetailView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'summary']
    permission_required = 'management.can_mark_returned'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'summary']
    permission_required = 'management.can_mark_returned'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
    permission_required = 'management.can_mark_returned'

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
    permission_required = 'management.can_mark_returned'

class WarehouseUpdateView(UpdateView):
    model = Warehouse
    fields = ['name', 'address']
    permission_required = 'management.can_mark_returned'

class WarehouseDeleteView(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('warehouses')
    permission_required = 'management.can_mark_returned'

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
    permission_required = 'management.can_mark_returned'

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['product', 'user', 'quantity', 'status']
    permission_required = 'management.can_mark_returned'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders')
    permission_required = 'management.can_mark_returned'

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
    permission_required = 'management.can_mark_returned'

class DeliveryUpdateView(UpdateView):
    model = Delivery
    fields = ['product', 'supplier', 'quantity', 'date']
    permission_required = 'management.can_mark_returned'

class DeliveryDeleteView(DeleteView):
    model = Delivery
    success_url = reverse_lazy('deliveries')
    permission_required = 'management.can_mark_returned'

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
    permission_required = 'management.can_mark_returned'

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = ['name', 'contact', 'address', 'tel']
    permission_required = 'management.can_mark_returned'

class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('suppliers')
    permission_required = 'management.can_mark_returned'
