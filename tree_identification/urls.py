from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from .views import register_user
from .views import login_user
from .views import logout_user
from .views import contact
from tree_identification import views as user_views

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
    path("profile/update/", views.profile_update, name="profile-update"),
    path("profile/delete/", views.profile_delete, name="profile-delete"),
    path("check_username/", views.check_username, name="check_username"),
    path("add_tree/", views.add_tree, name="add_tree"),
    path('my_trees/', views.my_trees, name='my_trees'),
]

# adapted from tutorial video:
# https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
