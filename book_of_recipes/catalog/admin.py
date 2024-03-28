from django.contrib import admin

from django.contrib import admin
from catalog.models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
                    'name_recipe', 
                    'description','date_of_creation', 'author',
                )
    list_display_links = ('name_recipe',)
    ordering = ('date_of_creation',  
                'name_recipe')
    list_per_page = 5
   
    prepopulated_fields = {'slug': ('name_recipe',)}
