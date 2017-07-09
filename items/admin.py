from django.contrib import admin

from .models import Item, Deal


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'added_on', 'is_active']


class DealAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'item', 'status']


admin.site.register(Item, ItemAdmin)
admin.site.register(Deal, DealAdmin)
