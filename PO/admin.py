from django.contrib import admin

# Register your models here.
from .models import PO, product

admin.site.register(PO)
admin.site.register(product)
