from carts.models import Favourite


def get_favorites_ricipes(request):
    if request.user.is_authenticated:
        return Favourite.objects.filter(user=request.user)
