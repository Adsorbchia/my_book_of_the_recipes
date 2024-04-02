
from django.urls import  path
from catalog import views

app_name = "catalog"

urlpatterns = [
    path('search/',views.show_catalog, name='search' ),
    path("category/<slug:category_slug>/", views.show_catalog, name="catalog"),
    path("recipe/<slug:recipe_slug>/", views.ShowRecipe.as_view(), name="recipe"),
    path("user-add-recipe/", views.AddPage.as_view(), name="user_add_recipe"),
    path(
        "change/<slug:slug>/", views.UpdatePage.as_view(), name="change_the_recipe"
    ),
    path("remove/<slug:slug>/", views.DeletePage.as_view(), name="remove"),
    ]
