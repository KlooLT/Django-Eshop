from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.application, name='application'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('create_product/', views.createProduct, name='create_product'),
    path('update_product/<str:pk>', views.updateProduct, name='update_product'),
    path('delete_product/<str:pk>', views.deleteProduct, name='delete_product'),


]
