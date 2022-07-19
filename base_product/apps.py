from django.apps import AppConfig


class BaseProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_product'
