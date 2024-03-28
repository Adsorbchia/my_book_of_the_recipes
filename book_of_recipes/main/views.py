from django.shortcuts import render
from catalog.models import Category, Recipe
from users.models import User



def index(request):
    categories = Category.objects.all()

    recipes = Recipe.objects.filter(cooking_time__lt=35)[:5]

    context = {
        "title": "COOKING at HOME - Главная",
        "content": "COOKING at HOME - книга полезных рецептов",
        "categories": categories,
        "recipes": recipes,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {"title": "COOKING at HOME - О нас"}
    return render(request, "main/about.html", context)


