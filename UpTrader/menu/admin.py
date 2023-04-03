from django.contrib import admin

from .models import Menu, Item


class MenuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'menu', 'parent')


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
