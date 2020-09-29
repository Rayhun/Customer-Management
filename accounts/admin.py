from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)

class OrderMoelAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer','Product','date_created','statur')

admin.site.register(Order, OrderMoelAdmin)

