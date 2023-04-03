from django.db import models


class Menu(models.Model):
    """
    Model for storing website menus.

    Fields:
    - title (CharField): title of the menu.
    - slug (SlugField): unique identifier of the menu for URLs.

    Methods:
    - __str__(): returns the title of the menu as a string.
    """
    title = models.CharField(max_length=200,
                             verbose_name='Menu title')
    slug = models.SlugField(max_length=200,
                            unique=True,
                            verbose_name='Menu slug')

    def __str__(self):
        return self.title


class Item(models.Model):
    """
    Model for storing menu items.

    Fields:
    - title (CharField): title of the menu item.
    - menu (ForeignKey): reference to the menu that the item belongs to.
    - parent (ForeignKey): reference to the parent item (if any).

    Methods:
    - __str__(): returns the title of the menu item as a string.
    """
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

    def __str__(self):
        return self.title
