"""App configuration for the stocks app."""

from django.apps import AppConfig


class StocksConfig(AppConfig):
    """Django app configuration for stocks."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "stocks"
