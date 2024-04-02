from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path
from users import views


app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "password-change/", views.UserPasswordChange.as_view(), name="password_change"
    ),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
        name="password_change_done",
    ),
    path("registration/", views.RegistrationUser.as_view(), name="registration"),
    path("user-settings/", views.user_settings, name="user_settings"),
    path("profile/", views.ShowProfile.as_view(), name="profile_user"),
    
    path("creators/", views.ShowAuthors.as_view(), name="creators"),
    path("creator/<int:user_id>/", views.ShowAuthorProfile.as_view(), name="creator"),
]
