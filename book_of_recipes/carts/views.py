from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.generic import ListView, TemplateView

from carts.models import Favourite, Subscribers

from catalog.models import Recipe
from users.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin


class ShowFavoriteRecipes(LoginRequiredMixin, ListView):

    template_name = "carts/favorite_recipes.html"
    context_object_name = "favourite"

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)


@login_required
def cart_add(request, recipe_id):

    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if recipe.favor_recipe.filter(user=request.user).exists():
        Favourite.objects.filter(user=request.user, recipe=recipe).delete()

    else:
        Favourite.objects.create(user=request.user, recipe=recipe)

    context = {
        "recipe": recipe,
    }

    return render(request, "catalog/recipe.html", context=context)



class UsersRecipesPage(LoginRequiredMixin, TemplateView):
    template_name = "carts/user_recipes.html"



# @login_required
# def users_recipes(request):
#     return render(request, "carts/user_recipes.html")


@login_required
def create_subscription(request, creator_id):
    creator = User.objects.get(pk=creator_id)
    subscribers = Subscribers.objects.filter(user=request.user, creator=creator)
    if subscribers.exists():
        subscribers.delete()
    else:
        Subscribers.objects.create(user=request.user, creator=creator)
    return redirect(request.META["HTTP_REFERER"])




def favorite_authors(request, user_id):
    user = User.objects.get(pk=user_id)
    authors = 0
    if user.subscriber.exists():
        authors = user.subscriber.all()
    context = {"title": "Подписки", "authors": authors}
    return render(request, "carts/favorite_authors.html", context)




def subscribers_of_the_user(request, user_id):
    user = User.objects.get(pk=user_id)
    subscribers = 0
    if user.writer.exists():
        subscribers = Subscribers.objects.filter(creator=user).all()
    context = {"title": "Подписчики", "subscribers": subscribers}
    return render(request, "carts/subscribers.html", context)
