from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('products', views.products, name='products'),
    path('clients', views.clients, name='clients'),
    path('sales', views.sales, name='sales'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('signin', views.sign_in, name='signin'),
    path('signup',views.sign_up, name='singup'),
    path('config', views.config, name='config'),
    path('logout', views.log_out, name='logout'),
]