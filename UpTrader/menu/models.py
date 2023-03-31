from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Menu title')
    slug = models.SlugField(max_length=200, verbose_name='Menu slug')

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Item title')
    menu = models.ForeignKey(Menu,
                             blank=True,
                             null=True,
                             related_name='items',
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='childrens',
                               on_delete=models.CASCADE)

    url = models.CharField(max_length=150, verbose_name='Item url')

    def __str__(self):
        return self.title
