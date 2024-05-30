from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cart'
    verbose_name = 'بخش سبد خرید'

    def ready(self):
        import apps.cart.signals
        return super().ready()
