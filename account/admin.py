from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Ivrepresentative)
admin.site.register(Branch)
admin.site.register(Invoice)

admin.site.register(Profile)
