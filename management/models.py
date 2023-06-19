from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
import uuid


class Product(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название товара")
    summary = models.CharField(max_length=1000, help_text="Введите краткое описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Введите цену товара")
    quantity = models.PositiveIntegerField(help_text="Введите количество товара")
    warehouse = models.ForeignKey("Warehouse", on_delete=models.CASCADE, help_text="Идентификатор склада", blank=True, null=True)
    time_added = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название категории товара")
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание категории")

    def get_absolute_url(self):
        """Returns the url to access a particular category instance."""
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.name)


class Category_Product(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
       return f"Category_Product #{self.id}"


class Warehouse(models.Model):
    products = models.ManyToManyField("Product", related_name='warehouses', blank=True)
    name = models.CharField(max_length=200, help_text="Введите название склада")
    address = models.CharField(max_length=200, help_text="Введите адрес склада")

    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return reverse('warehouse-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.name)


class Order(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(help_text="Введите количество товара")
    date = models.DateField(auto_now_add=True, help_text="Время создания заказа")
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return reverse('order-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.name)

class Delivery(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    supplier = models.ForeignKey("Supplier", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(help_text="Введите количество поставляемого товара")
    date = models.DateField(help_text="Выберите дату поставки")

    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return reverse('delivery-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.name)

class Supplier(models.Model):
    name = models.CharField(max_length=200, help_text="Введите наименование организации")
    contact = models.CharField(max_length=200, help_text="Введите контактное лицо")
    address = models.CharField(max_length=200, help_text="Введите адрес поставщика")
    tel = models.CharField(max_length=20, help_text="Введите номер телефона")


    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return reverse('supplier-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.name)




