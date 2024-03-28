from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from catalog.models import Recipe


def q_search(query):
    if query.isdigit() and len(query) <= 3:
        return Recipe.objects.filter(cooking_time=int(query))

    vector = SearchVector("name_recipe", "cooking_steps")
    query = SearchQuery(query)
    return (
        Recipe.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
