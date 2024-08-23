from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Pages(models.Model):

    class Meta:
        verbose_name_plural = 'Pages'
        verbose_name = 'Page'
        ordering = ['order', 'title']

    
    title = models.CharField(max_length=200, verbose_name='Título')
    content =RichTextField(verbose_name='Contendio')
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.title
    