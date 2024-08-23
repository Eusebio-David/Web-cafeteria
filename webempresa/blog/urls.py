from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("blog/", views.blog, name='blog'),
    path('blog/category/<int:category_id>/', views.category, name='category'),

]
