from django.apps import AppConfig

from data.common.auto_admin_register import auto_register_admin_models


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data.common'

    def ready(self):
        auto_register_admin_models()
