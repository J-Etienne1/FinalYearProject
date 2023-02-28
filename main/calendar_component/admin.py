from django.contrib import admin
from . import models


class EventsAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(models.Booking, EventsAdmin)