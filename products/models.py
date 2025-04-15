from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name='nombre')
    description = models.TextField(max_length=300, verbose_name='descripcion')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='products', null=True, blank=True)
    calification = models.IntegerField(verbose_name='calificacion', null=True, blank=True)

    def __str__(self):
        return self.name