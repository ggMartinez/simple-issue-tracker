from .custom_admin import custom_admin
from django.contrib import admin
from django.contrib.auth.models import User, Group


from .models import Ticket



class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'status']

    list_filter = ['status']

    def add_view(self, request, form_url='', extra_context=None):
        self.exclude = ['author',]
        self.readonly_fields = ('status',)
        return super(TicketAdmin, self).add_view(request)

    def change_view(self, request, object_id, form_url='', ):
        self.readonly_fields = ('author',)
        return super(TicketAdmin, self).change_view(request, object_id,
            form_url)


    

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


custom_admin.register(Ticket, TicketAdmin)
custom_admin.register(User)
custom_admin.register(Group)