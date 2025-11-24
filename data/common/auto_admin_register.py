from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered


def auto_register_admin_models():
    """
    Automatically registers all Django models in the project with the admin site.

    For each model discovered via `apps.get_models()`, this function dynamically
    creates an admin class (`AutoAdmin`) with the following behavior:

        - list_display: Shows all model fields in the Django admin list view,
          making every field visible without manually defining admin classes.

        - search_fields: Enables search across all fields listed in `list_display`.

    If a model is already registered, the `AlreadyRegistered` exception is caught
    and ignored to avoid duplicate-registration errors.

    This utility function is useful during development or for small projects
    where manually creating admin classes for each model is unnecessary.
    """

    for model in apps.get_models():
        try:
            class AutoAdmin(admin.ModelAdmin):
                list_display = [field.name for field in model._meta.fields]
                search_fields = list_display

            admin.site.register(model, AutoAdmin)
        except AlreadyRegistered:
            pass
