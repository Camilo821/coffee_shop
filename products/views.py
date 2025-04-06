from django.shortcuts import render
from django.views import generic
from .forms import ProductForm
# Create your views here.
class ProductFormView(generic.FormView):
    template_name = 'prdoucts/add_product.html'
    form_class = ProductForm