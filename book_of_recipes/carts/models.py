from django.db import models
from django.db import models
from catalog.models import Recipe
from users.models import User
from django.contrib.auth import get_user_model


class FavouriteQuerySet(models.QuerySet):
    def total_number(self):
        if self:
            return sum(1 for _ in self)
        return 0


class Favourite(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        related_name="aut_user",
    )
    recipe = models.ForeignKey(
        Recipe,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="рецепт",
        related_name="favor_recipe",
    )

    class Meta:
        db_table = "favourite"
        verbose_name = "избранное"
        verbose_name_plural = "избранное"

    def __str__(self):
        return f"Избранное {self.user.username} | Рецепт {self.recipe.name_recipe}"
  

    objects = FavouriteQuerySet.as_manager()


class Subscribers(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="подписчик",
        related_name="subscriber",
    )
    creator = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="автор",
        related_name="writer",
    )

    class Meta:
        db_table = "subscribers"
        verbose_name = "подписки"
        verbose_name_plural = "подписки"

    def __str__(self):
        return {self.user}

    objects = FavouriteQuerySet.as_manager()
