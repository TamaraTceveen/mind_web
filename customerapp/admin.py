from django.contrib import admin

from customerapp.models import Customer, Order

admin.site.register(Customer)
admin.site.register(Order)
