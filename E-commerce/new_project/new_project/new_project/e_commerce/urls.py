from django.urls import path
from .views import *  # Importing specific views
from django.contrib.auth import views as auth_views
from . import views  # Importing the views module to access other views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('product/<int:id>/', product_detail_view, name='product_detail'),
    path('products/', all_products_view, name='all_products'),
    path('register/', views.register, name='register'),  # Registration view
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Django's built-in login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django's built-in logout view
    path('profile/', profile, name='profile'),  # Profile view
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('orders/',orders_view, name='orders'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'), 
    path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('process_order/', views.process_order, name='process_order'),
    path('', views.store, name='store'),
    path('order/<int:product_id>/', views.order_product, name='order_product'), 
    path('order-success/', views.order_success, name='order_success'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
  
  
     

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
