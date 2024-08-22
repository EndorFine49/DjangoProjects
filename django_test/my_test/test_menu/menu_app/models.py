from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField('Название', max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def children(self):
        return self.__class__.objects.filter(parent=self.id)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=('position,')
        verbose_name='Пункт меню'
        verbose_name_plural= 'Пункты меню'