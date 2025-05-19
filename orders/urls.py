from .views import MyOrderView
from django.urls import path

urlpatterns = [
    path('my-order', MyOrderView.as_view(), name='my_order')
]