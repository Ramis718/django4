from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/data/', views.index),
    path('api/v1/product/', views.product_list_view),
    path('api/v1/product/<int:id>/', views.product_datail_view), 
    
]
