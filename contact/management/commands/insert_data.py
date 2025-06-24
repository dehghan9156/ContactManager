from faker import Faker
from ...models import Contact
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    def handle(self,*args,**options):
        faker = Faker()
        for _ in range(6):
            Contact.objects.create(
                    name = faker.first_name(),
                    family = faker.last_name(),
                    gender = faker.random_choices(['man','woman','unknown']),
                    job = faker.job(),
                    phone = str(faker.phone_number())
            )
