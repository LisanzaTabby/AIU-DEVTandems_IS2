from django.apps import AppConfig


class AiuappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AIUApp'

    def ready(self):
        import AIUApp.signals
