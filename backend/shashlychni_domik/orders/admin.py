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

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'method' ]
    lest_display_links = ['id', 'method']

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status' ]
    lest_display_links = ['id', 'status']

class PromotionalCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'user', 'discount' ]
    lest_display_links = ['id', 'code' ]
    search_fields = ['code']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'street', 'house', 'frame', 'structure', 'floor', 'apartment', 'code' ]
    lest_display_links = ['id' ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'anonymous', 'user', 'name', 'surname', 'phone', 'email', 'date_create', 'address', 'date_delivery', 'status', 'promotional_code', 'cutlery', 'comment' ]

admin.site.register(Dish, DishAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(PromotionalCode, PromotionalCodeAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)