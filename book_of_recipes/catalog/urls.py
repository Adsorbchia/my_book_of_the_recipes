
from django.urls import  path
from catalog import views

app_name = "catalog"

urlpatterns = [
    path('search/',views.catalog, name='search' ),
    path("<slug:category_slug>/", views.catalog, name="catalog"),
    path("recipe/<slug:recipe_slug>/", views.recipes, name="recipe"),
    ]
