from django.urls import path
from .views import ProductFormView
from .views import SuccessFormView

urlpatterns = [
    path('agregar', ProductFormView.as_view(), name='add_product'),
    path('', SuccessFormView.as_view(), name='list_product')
]
