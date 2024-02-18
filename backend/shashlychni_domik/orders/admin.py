from django.contrib import admin
from .models import Dish, Section, PaymentMethod, OrderStatus, PromotionalCode, Address, Order
# Register your models here.

class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section', 'image', 'count', 'price', 'isActive', 'isBestseller', 'isNew']
    lest_display_links = ['id', 'name']
    search_fields = ['id', 'name']
    list_editable = ['isActive', 'isBestseller', 'isNew']
    
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' ]
    lest_display_links = ['id', 'name']
    search_fields = ['id', 'name']

admin.site.register(Dish, DishAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(PaymentMethod)
admin.site.register(OrderStatus)
admin.site.register(PromotionalCode)
admin.site.register(Address)
admin.site.register(Order)