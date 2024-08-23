from django.shortcuts import render
from .models import Services
# Create your views here.

def servicesView(request):
    template_name = 'core/services.html'
    list_services = Services.objects.order_by('created')
    return render(request, template_name, {'list_services': list_services} )
