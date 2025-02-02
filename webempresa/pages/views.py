from django.shortcuts import render, get_object_or_404
from .models import Pages

# Create your views here.
def page(request, page_id, page_slug):
    template_name = 'pages/sample.html'
    page = get_object_or_404(Pages, id=page_id)
    return render(request, template_name, {'page': page})