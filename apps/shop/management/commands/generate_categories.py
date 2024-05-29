from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from apps.shop.models import ProductCategoryModel


class Command(BaseCommand):
    help = 'Generate fake categories'

    def handle(self, *args, **options):
        fake = Faker(locale="fa_IR")
        for _ in range(10):
            title = fake.word()
            slug = slugify(title, allow_unicode=True)
            ProductCategoryModel.objects.get_or_create(title=title, slug=slug)
        self.stdout.write(self.style.SUCCESS('Successfully generated 10 fake categories'))
