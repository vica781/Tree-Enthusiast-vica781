from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from tree_identification import views as user_views
from .views import (
    home,
    register_user,
    login_user,
    logout_user,
    contact,
    add_tree,
    my_trees,
    tree_detail,
    edit_tree,
    delete_tree,
    search_trees,
    browse_trees,
    contact_success,
)

urlpatterns = [
    path("admin/", admin.site.urls),
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
    path("logout/", views.logout_user, name="logout"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profile_user, name="profile"),
    path("profile/update/", views.profile_update, name="profile-update"),
    path("profile/delete/<int:user_id>/", views.profile_delete, name="profile_delete"),
    path("check_username/", views.check_username, name="check_username"),
    path("check_email/", views.check_email, name="check_email"),
    # Updated tree paths
    path("tree/add/", views.add_or_edit_tree, name="add_tree"),
    path("tree/edit/<int:tree_id>/", views.add_or_edit_tree, name="edit_tree"),
    path("my_trees/", views.my_trees, name="my_trees"),
    path("tree/<int:tree_id>/", views.tree_detail, name="tree_detail"),
    path("tree/delete/<int:tree_id>/", views.delete_tree, name="delete_tree"),
    path(
        "identification_guide/", views.identification_guide, name="identification_guide"
    ),
    path("search/", views.search_trees, name="search_trees"),
    path("browse_trees/", views.browse_trees, name="browse_trees"),
    path("contact_success/", views.contact_success, name="contact_success"),
]

# Include these if you're using Django's static and media file serving in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
