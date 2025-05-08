from multiprocessing import context
from pyexpat.errors import messages
from altair import Order
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, ProfileForm
from .models import Profile
from django.views.generic.edit import UpdateView ,DeleteView ,CreateView
from django.urls import reverse_lazy
from .forms import SimpleUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import login

from .models import Order, Product, OrderItem, Profile



def home_view(request):
    return render(request, 'home.html')  

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def all_products_view(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})

from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def orders_view(request):
    orders = Order.objects.all()
    orderItems = OrderItem.objects.all()
    return render(request, 'orders/orders_page.html', {"orders": orders, "orderItems": orderItems})


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # Ensure the user has a profile
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login") 
    else:
        form = SimpleUserCreationForm()
    return render(request, "register.html", {"form": form})


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock', 'ratings', 'ratingsCount', 'img', 'shipping', 'quantity', 'category']  
    template_name = 'products/add_products.html'  
    success_url = reverse_lazy('all_products')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock', 'ratings', 'ratingsCount', 'img', 'shipping', 'quantity', 'category']
    template_name = 'products/update_product.html'  
    success_url = reverse_lazy('all_products')
     

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'  
    success_url = reverse_lazy('all_products')


@login_required
def cart(request):
    try:
        order = Order.objects.get(user=request.user, complete=False)
    except Order.DoesNotExist:
        order = Order.objects.create(user=request.user, complete=False)

    items = order.orderitem_set.all()  

    context = {
        'order': order,
        'items': items,
    }
    return render(request, 'cart/cart.html', context)  

def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        product = get_object_or_404(Product, id=product_id)
        order, created = Order.objects.get_or_create(user=request.user, complete=False)

        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        order_item.quantity = quantity
        order_item.save()

        return redirect('cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order = Order.objects.get(user=request.user, complete=False)
    order_item = OrderItem.objects.filter(order=order, product=product).first()

    if order_item:
        order_item.delete()

    return redirect('cart')

from django.contrib import messages

def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        order = Order.objects.get(user=request.user, complete=False)
    except Order.DoesNotExist:
        order = None

    if order is None:
        return render(request, 'empty_cart.html')

    items = order.orderitem_set.all()

    total_items = sum(item.quantity for item in items)
    total_price = sum(item.get_total() for item in items)
    shipping_cost = sum(item.product.shipping for item in items)
    total_with_shipping = total_price + shipping_cost

    context = {
        'order': order,
        'items': items,
        'total_items': total_items,
        'total_price': total_price,
        'shipping_cost': shipping_cost,
        'total_with_shipping': total_with_shipping,
    }

    return render(request, 'cart.html', context)





def process_order(request):
    if request.user.is_authenticated:
        order = Order.objects.get(user=request.user, complete=False)
        

        order.complete = True
        order.save()
        order.orderitem_set.all().delete()

        return redirect('order_success') 
    else:
        return redirect('login') 
    


@login_required
def checkout(request, product_id=None):
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    items = order.orderitem_set.all()  
    product = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order, user=request.user)  
        if form.is_valid():
            order = form.save(commit=False)
            order.complete = True  
            order.save()
            items.delete() 

            return redirect('order_success')  
    else:
      
        form = OrderForm(instance=order, user=request.user)  

    context = {
        'items': items,
        'order': order,
        'form': form,
        'product': product,
    }
    return render(request, 'cart/checkout.html', context)
def store(request):
    products = Product.objects.all() 
    context = {'products': products}
    return render(request, 'store/store.html', context)
@login_required 
def order_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        return redirect('order_success')  
    
    context = {'product': product}
    return render(request, 'cart/order_form.html', context)
def order_success(request):
    return render(request, 'cart/order_success.html')



def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.save()
    return redirect('cart')

from django.shortcuts import render
from .models import Product

def category_view(request, category_name):

    products_by_category = Product.objects.filter(category=category_name)
    
    context = {
        'products': products_by_category,
        'category_name': category_name
    }
    return render(request, 'products/category.html', context)




@login_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):  
            order.status = new_status
            order.save()
    return redirect('orders_page')  

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.is_superuser:
        order.delete()
    return redirect('orders_page')  

def order_management(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders_page.html', {'orders': orders})