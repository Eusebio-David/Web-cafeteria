from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path("page/<int:page_id>/<slug:page_slug>/", views.page, name='page'),
]

