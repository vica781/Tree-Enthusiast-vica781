from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home
from . import views
from .views import register_user
from .views import login_user
from .views import logout_user
from .views import contact


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("logout/", logout_user, name="logout"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profile_user, name="profile"),
]
