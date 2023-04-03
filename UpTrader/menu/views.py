from django.shortcuts import render, get_object_or_404

from .models import Menu


def index_menu_page(request):
    """
    A view function to display a list of all menus.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered template and the list of menus.

    """
    list_menu = Menu.objects.all()
    template_name = 'menu/index.html'
    return render(request, template_name, {'list_menu': list_menu})


def single_menu_page(request, slug):
    """
    A view function to display the details of a single menu.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The unique slug of the menu.

    Returns:
        HttpResponse: The HTTP response object with the rendered template
        and the menu details.

    Raises:
        Http404: If the menu with the given slug does not exist.

    """
    menu = get_object_or_404(Menu, slug=slug)
    context = {'menu_name': menu.title}
    template_name = 'menu/menu_single_page.html'
    return render(request, template_name, context)
