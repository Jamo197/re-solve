from django.contrib import admin
from .models import Article, Material, Property, SustainabilityProperty

admin.site.register(Article)
admin.site.register(Material)
admin.site.register(Property)
admin.site.register(SustainabilityProperty)
