from django.db import models


class Menu(models.Model):
    name = models.CharField(
        'Название', max_length=100)
    description = models.TextField(
        'Описание', max_length=300, blank=True)


    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(
        'Пункт меню', max_length=100)
    url = models.CharField(
        verbose_name='URL-адрес стороннего ресурса',
        help_text=(
            'Указывается для перехода на ресурс из конечного пункта меню, '
            'если не указать, то алгоритм будет пытаться найти потомков '
            'данного пункта меню и создать из них подменю'),
        max_length=50, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name
