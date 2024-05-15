from django.apps import AppConfig


class CharactermanagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "characterManager"
    
    def ready(self):
        import characterManager.signals 