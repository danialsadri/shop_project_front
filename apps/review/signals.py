from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ReviewModel, ReviewStatusType


@receiver(post_save, sender=ReviewModel)
def calculate_avg_review(sender, instance, created, **kwargs):
    if instance.status == ReviewStatusType.accepted.value:
        product = instance.product
        average_rating = ReviewModel.objects.filter(product=product, status=ReviewStatusType.accepted).aggregate(Avg('rate'))['rate__avg']
        product.avg_rate = round(average_rating, 1)
        product.save()
