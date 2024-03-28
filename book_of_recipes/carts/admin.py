from django.contrib import admin

from carts.models import Favourite



class FavouriteTabAdmin(admin.TabularInline):
    model = Favourite
    fields = [
        "user",
        "recipe",
    ]
    extra = 1


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "recipe",
    ]
    search_fields = [
        "user__first_name",
        "user__last_name",
        "recipe_recipe_name",
        "recipe__description",
    ]
