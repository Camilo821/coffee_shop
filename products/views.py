from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import ProductForm
from products.models import Product
# Create your views here.


class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessFormView(generic.ListView):
    model = Product
    template_name = 'products/success.html'
    context_object_name = 'products'
