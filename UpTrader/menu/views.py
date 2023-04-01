from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect

from .models import Menu




def index_menu_page(request):
    list_menu = Menu.objects.all()
    template_name = 'menu/index.html'
    return render(request, template_name, {'list_menu': list_menu})


def single_menu_page(request, slug):
    menu = get_object_or_404(Menu, slug=slug)
    context = {'menu_name': menu.title}
    template_name = 'menu/menu_single_page.html'
    return render(request, template_name, context)