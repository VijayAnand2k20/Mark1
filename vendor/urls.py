from django.contrib.auth import views as authViews

from django.urls import path
from . import views

app_name = 'vendor'
urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name="vendor_admin"),
    path('add-product/', views.add_product, name='add_product'),

    path('login/',authViews.LoginView.as_view(template_name='vendor/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout')
]