from django.contrib import admin

from .models import Order, Request

admin.site.register(Order)
admin.site.register(Request)