from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from catalog.models import Recipe

from .forms import UserRecipeForm


class ShowRecipe(DetailView):
    model = Recipe
    template_name = "catalog/recipe.html"
    slug_url_kwarg = "recipe_slug"
    context_object_name = "recipe"


class AddPage(CreateView):
    form_class = UserRecipeForm
    template_name = "catalog/user_add_recipe.html"


class UpdatePage(UpdateView):
    model = Recipe
    fields = [
        "name_recipe",
        "description",
        "ingredients",
        "cooking_steps",
        "cooking_time",
        "image",
        "category",
    ]
    template_name = "catalog/change_the_recipe.html"


class DeletePage(DeleteView):
    model = Recipe
    success_url = reverse_lazy("main:index")
    context_object_name = "recipe"


def show_catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    on_image = request.GET.get("on_image", None)
    order_by = request.GET.get("order_by", None)

    if category_slug == "all":
        recipes = Recipe.objects.all()
        if on_image:
            recipes = Recipe.objects.exclude(image="")
        if order_by and order_by != "default":
            recipes = Recipe.objects.order_by(order_by)
        if on_image and order_by and order_by != "default":
            recipes = Recipe.objects.order_by(order_by).exclude(image="")

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
        if on_image and order_by and order_by != "default":
            recipes = (
                Recipe.objects.filter(category__slug=category_slug)
                .order_by(order_by).exclude(image="")
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
