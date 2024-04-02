from django.urls import path
from carts import views


app_name = "carts"

urlpatterns = [
    path("favorite-recipes/", views.ShowFavoriteRecipes.as_view(), name="favorite_recipes"),
    path("cart-add/<int:recipe_id>/", views.cart_add, name="cart_add"),
    path("users-recipes/", views.UsersRecipesPage.as_view(), name="users_recipes"),
    path(
        "create-subscription/<int:creator_id>/",
        views.create_subscription,
        name="create_subscription",
    ),
    path(
        "favorite-authors/<int:user_id>/",
        views.favorite_authors,
        name="favorite_authors",
    ),
    path(
        "subscribers/<int:user_id>/", views.subscribers_of_the_user, name="subscribers"
    ),
]
