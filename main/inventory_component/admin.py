from django.contrib import admin
from . import models


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item',)


admin.site.register(models.Inventory, InventoryAdmin)