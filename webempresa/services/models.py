from django.db import models

# Create your models here.

class Services(models.Model):

    class Meta: 
        verbose_name_plural = 'Services'
        verbose_name = 'Service'
        ordering = ['-created']

    title = models.CharField(max_length=200, blank = True, null= True, verbose_name='Título' )
    subtitle = models.CharField(max_length=200, blank = True, null = True,verbose_name='Subtítulo' )
    content = models.TextField(verbose_name='Contenido' )
    image = models.ImageField(verbose_name='imagen', upload_to='imagen-services' )
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación' )
    update = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición' )



    def __str__(self):
        return self.title
    
