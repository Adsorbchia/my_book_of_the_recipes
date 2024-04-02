from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models import F

from .models import User
from catalog.models import Recipe
from users.forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserProfileForm,
    UserPasswordChageForm,
)
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}

    def get_success_url(self) -> str:
        return reverse_lazy("main:index")


class RegistrationUser(CreateView):
    form_class = UserRegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("user:login")


# def registration(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.instance
#             auth.login(request, user)
#             messages.success(request, f"{user.username}, вы успешно зарегестрированы!")
#             return HttpResponseRedirect(reverse("main:index"))
#     else:
#         form = UserRegistrationForm()
#     context = {"title": "Регистрация", "form": form}
#     return render(request, "users/registration.html", context)


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

            return HttpResponseRedirect(reverse("user:user_settings"))
    else:
        form = UserProfileForm(instance=request.user)

    context = {"title": "Кабинет", "form": form}
    return render(request, "users/user_settings.html", context)




class ShowProfile(LoginRequiredMixin, ListView):
    model = auth.get_user_model()

    template_name = "users/user_profile.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)




class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChageForm
    success_url = reverse_lazy("user:password_change_done")
    template_name = "users/password_change_form.html"




class ShowAuthors(ListView):
    model = auth.get_user_model()
    template_name = "users/creators.html"
    context_object_name = "creators"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        creators = [
            creator for creator in context["object_list"] if creator.authors.exists()
        ]
        context["creators"] = creators
        return context




class ShowAuthorProfile(ListView):
    template_name = "users/creators_profile.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(author__id=self.kwargs["user_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creator"] = auth.get_user_model().objects.filter(
            pk=context["recipes"][0].author.pk
        )
        return context
