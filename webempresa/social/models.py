from django.db import models

# Create your models here.
class Link(models.Model):

    class Meta:
        verbose_name_plural = 'Links'
        verbose_name = 'Link'
        ordering = ['-created']

    key = models.SlugField(verbose_name='nombre clave', max_length=100, unique=True)
    name = models.CharField(max_length=200, verbose_name='Red Social')
    url =models.URLField(verbose_name='enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.name
    
    