from django.apps import AppConfig


class TreeIdentificationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tree_identification"

    def ready(self):
        import tree_identification.signals


class UserConfig(AppConfig):
    name = "users"

    def ready(self):
        import tree_identification.signals
