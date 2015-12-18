from django.contrib.admin import AdminSite
from django.views.decorators.cache import never_cache
from .models import Ticket
from django.shortcuts import render_to_response


class CustomAdminSite(AdminSite):

    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        return urls

    @never_cache
    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}

        show_all = False

        if request.GET and 'show' in request.GET:
            if request.GET['show'] == 'all':
                show_all = True

        if show_all:
            tickets = Ticket.objects.filter(
                asignee=request.user).order_by('created_date')
        else:
            tickets = Ticket.objects.filter(asignee=request.user).filter(
                status='O').order_by('created_date')

        context = {
            'tickets': tickets,
            'show_all': show_all,
        }
        context.update(extra_context or {})
        return super(CustomAdminSite, self).index(request, context)


custom_admin = CustomAdminSite()
