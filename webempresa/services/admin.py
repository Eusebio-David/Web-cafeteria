from django.contrib import admin
from .models import Services

# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):

    readonly_fields = ('created','update')
    list_display = ['title', 'content']


