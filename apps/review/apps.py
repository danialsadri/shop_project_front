from django.apps import AppConfig


class ReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.review'
    verbose_name = 'بخش بازدید'

    def ready(self):
        import apps.review.signals
