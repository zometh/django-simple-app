from django.contrib import admin
from .models import  Pizza
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom']
    search_help_text = ["nom"]

admin.site.register(Pizza, PizzaAdmin)