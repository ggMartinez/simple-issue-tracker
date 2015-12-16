from django.contrib import admin
from .models import Ticket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user.username
        obj.save()

admin.site.register(Ticket, TicketAdmin)