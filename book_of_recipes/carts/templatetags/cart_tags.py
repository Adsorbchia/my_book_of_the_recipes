from django import template

from carts.models import Favourite, Subscribers
from carts.utils import get_favorites_ricipes
from catalog.models import Recipe
from users.models import User


register = template.Library()

@register.simple_tag()
def favorites_recipes(request):
    return get_favorites_ricipes(request)

@register.simple_tag()
def user_recipe(user_id):
  if Recipe.objects.filter(author=user_id):
      return Recipe.objects.filter(author=user_id)
  return 0


@register.simple_tag()
def total_number_of_favorites(slug_recipe):
    recipe = Recipe.objects.get(slug=slug_recipe)
    return Favourite.objects.filter(recipe=recipe).all()


@register.simple_tag()
def quantity_favorite_authors(user_id):
   user = User.objects.get(pk=user_id)
   if user.subscriber.exists():
        quantity = user.subscriber.count()
        return quantity
   else:
        return 0

@register.simple_tag()
def quantity_subscribers(user_id):
   user = User.objects.get(pk=user_id)
   if user.writer.exists():
        quantity = Subscribers.objects.filter(creator=user).all().count()
        return quantity
   else:
       return 0
   

@register.simple_tag()
def checking_for_a_subscription(request, user_id):
    creator = User.objects.get(pk=user_id)
    if request.user.subscriber.exists() and Subscribers.objects.filter(user=request.user, creator=creator):
        return 1
    elif request.user.writer.exists() and Subscribers.objects.filter(user=creator, creator=request.user):
        return 2
    return 0 
    

@register.simple_tag()
def checking_for_a_favorites(request, recipe_id):
    if request.user.aut_user.exists() and Favourite.objects.filter(user=request.user, recipe=recipe_id):
        return True
    else:
        return False
