from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


def translit_to_eng(s: str):
    d = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "yo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "",
        "ы": "y",
        "ъ": "",
        "э": "r",
        "ю": "yu",
        "я": "ya",
    }
    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class Recipe(models.Model):
    name_recipe = models.CharField(
        max_length=200, unique=True, verbose_name="Название рецепта"
    )
    slug = models.SlugField(
        max_length=300, unique=True, verbose_name="URL", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True, 
                                   null=True)
    ingredients = models.CharField(
        max_length=300, blank=True, null=True, verbose_name="ингредиенты"
    )
    cooking_steps = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.IntegerField(verbose_name="Время приготовления")
    image = models.ImageField(upload_to="recipe_image", blank=True, null=True)
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="category"
    )
    date_of_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления рецепта"
    )
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name="Автор", 
        related_name="authors"
    )
    class Meta:
        db_table = "recipe"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name_recipe

    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.name_recipe))
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("recipe_catalog:recipe", kwargs={"recipe_slug": self.slug})
