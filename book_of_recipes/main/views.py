from django.views.generic import ListView, TemplateView
from catalog.models import Recipe


class MainPage(ListView):
    template_name = "main/index.html"
    context_object_name = "recipes"
    title_page = "COOKING at HOME - Главная"
    paginate_by = 5

    def get_queryset(self):
        return Recipe.objects.filter(cooking_time__lt=35)


class AboutPage(TemplateView):
    template_name = "main/about.html"
    title_page = "COOKING at HOME - О нас"
