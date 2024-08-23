from django import template #registrarlo dentro de la libreria de templates 
from pages.models import Pages


"""
    creamos un tag simple y lo registramos
    en la libreria de templates
    
"""
register = template.Library()

@register.simple_tag 
def get_page_list():
    pages = Pages.objects.all()
    return pages 