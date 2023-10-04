from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User
from django_seed import Seed
from store import models as store_models


class Command(BaseCommand):
    help ='This class is use to create users by using command'
    def add_arguments(self, parser) :
        parser.add_argument(
            '--number', type=int, default=1, help='Creating users'
        )
    
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, number)
        seeder.execute()
        
        self.stdout.write(self.style.SUCCESS(f'{number} of users has been created'))