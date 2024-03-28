from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from catalog.models import Recipe
from users.forms import (
    UserLoginForm,
    # UserRecipeForm,
    UserRegistrationForm,
    UserProfileForm,
)


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, добро пожаловать!")
                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse("user:logout"):
                    return HttpResponseRedirect(request.POST.get("next"))

                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()
    context = {"title": "Авторизация", "form": form}
    return render(request, "users/login.html", context)



def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, вы успешно зарегестрированы!")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()
    context = {"title": "Регистрация", "form": form}
    return render(request, "users/registration.html", context)



@login_required
def user_settings(request):
    if request.method == "POST":
        form = UserProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, "Ваш профиль успешно обновлен")
            return HttpResponseRedirect(reverse("user:user_settings"))
    else:
        form = UserProfileForm(instance=request.user)

    context = {"title": "Кабинет", "form": form}
    return render(request, "users/user_settings.html", context)



@login_required
def show_profile(request):
    recipes = Recipe.objects.filter(author=request.user)
 
    context = {
        "title": "COOKING at HOME - Страница пользователя",
       
        "recipes": recipes

    }
    return render(request, 'users/user_profile.html', context=context)

@login_required
def logout(request):
    messages.success(
        request,
        f"{request.user.username}, спасибо что были с нами, возвращайтесь скорее!",
    )
    auth.logout(request)
    return redirect(reverse("main:index"))


# @login_required
# def add_recipe(request):
#     user = request.user
#     if request.method == "POST":
#         form = UserRecipeForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Ваш рецепт успешно добавлен")
#             return HttpResponseRedirect(reverse("main:index"))
#     else:
#         form = UserRecipeForm()

#     context = {"title": "Добавление рецепта", "user": user, "form": form}
#     return render(request, "users/user_add_recipe.html", context)



# @login_required
# def change_the_recipe(request, slug_recipe):
#     recipe = Recipe.objects.get(slug=slug_recipe)
#     if request.method == "POST":
#             form = UserRecipeForm(data=request.POST,instance=recipe, files=request.FILES)
#             if form.is_valid:
#                 form.save()
#                 messages.success(request, "Ваш рецепт отредактирован")
#                 return HttpResponseRedirect(reverse("main:index"))
#     else:
#         form = UserRecipeForm(instance=recipe)

#     context = {"title": "Редактирование рецепта", 
#                "recipe": recipe,
#                    "form": form}
#     return render(request, "users/change_the_recipe.html", context)



# @login_required
# def remove_the_recipe(request, slug_recipe):
#     recipe = Recipe.objects.get(slug=slug_recipe)
#     on_delete = request.GET.get("on_delete")
#     if on_delete == 'option1':
#         recipe.delete()
#         messages.success(request, "Ваш рецепт удалён")
#         return HttpResponseRedirect(reverse("main:index"))

#     context = {"title": "Удаление рецепта", 
#                "recipe": recipe}
#     return render(request, 'users/remove_the_recipe.html', context)
