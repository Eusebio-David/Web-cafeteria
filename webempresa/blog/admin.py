from django.contrib import admin
from .models import Category, Post

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['title', 'content', 'published', 'author', 'post_categories']
    ordering = ('author', 'published')
    search_fields = ('title','content','author__username', 'categories__name')
    date_hierarchy = 'published' #jeraquia, muestra el contendio jerarquizado
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        #el objeto hara referencia a cada elemento de la instacia, se recorre para cada objeto
        return ", ".join(c.name for c in obj.categories.all().order_by('name'))

    post_categories.short_description = 'Categorías'