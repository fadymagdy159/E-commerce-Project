from django.db import models
from django.contrib.auth.models import User  # Import User model

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    seller = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    ratings = models.IntegerField()
    ratingsCount = models.IntegerField()
    img = models.URLField(max_length=200)
    shipping = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username



class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash_on_delivery', 'Cash on Delivery')
    ]

    STATUS_CHOICES = [
        ('Received', 'Received'),
        ('In-delivery', 'In-delivery'),
        ('Delivered', 'Delivered')
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    shipping_address = models.CharField(max_length=255, null=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='credit_card')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Received')

    def __str__(self):
        return f"Order {self.id} - {self.status}"
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        if self.product is not None:
            return self.product.price * self.quantity
        return 0
