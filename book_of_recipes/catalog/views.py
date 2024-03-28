from django.shortcuts import render

from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from catalog.models import Recipe
from catalog.utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    on_image = request.GET.get("on_image", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        recipes = Recipe.objects.all()
        if on_image:
            recipes = Recipe.objects.exclude(image="")
        if order_by and order_by != "default":
            recipes = Recipe.objects.order_by(order_by)
    elif query:
        recipes = q_search(query)
    else:
        recipes = get_list_or_404(Recipe, category__slug=category_slug)
        if on_image:
            recipes = Recipe.objects.filter(category__slug=category_slug).exclude(
                image=""
            )
        if order_by and order_by != "default":
            recipes = Recipe.objects.filter(category__slug=category_slug).order_by(
                order_by
            )

    paginator = Paginator(recipes, 6)
    current_page = paginator.page(int(page))
    slug_url = category_slug
    context = {
        "title": "Cooking at home - все рецепты ",
        "recipes": current_page,
        "slug_url": slug_url,
    }
    return render(request, "catalog/catalog.html", context)


def recipes(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    context = {"recipe": recipe}
    return render(request, "catalog/recipe.html", context=context)
