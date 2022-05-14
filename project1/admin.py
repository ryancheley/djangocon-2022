from django.contrib import admin
from .models import member, PurchaseOrderDetail

# Register your models here.

admin.site.register(member)
admin.site.register(PurchaseOrderDetail)