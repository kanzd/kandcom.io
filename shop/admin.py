from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.user)
admin.site.register(models.cart)
admin.site.register(models.pcart)