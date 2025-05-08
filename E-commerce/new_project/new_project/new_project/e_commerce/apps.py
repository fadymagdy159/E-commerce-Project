from django.apps import AppConfig

class ECommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e_commerce'

    def ready(self):
        import e_commerce.signals  # Ensure this import is in place
