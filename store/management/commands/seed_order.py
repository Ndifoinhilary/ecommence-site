from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User
from django_seed import Seed
from store import models as store_models
import random

NAME = 'Order'

class Command(BaseCommand):
    help =f'This class is use to create {NAME} by using command'
    def add_arguments(self, parser) :
        parser.add_argument(
            '--number', type=int, default=1, help='Creating {NAME}'
        )
    
    def handle(self, *args, **options):
        number = options.get('number')
        all_users = store_models.Customer.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(store_models.Order, number,{
            'customer':lambda x: random.choice(all_users),
        })
        seeder.execute()
        
        self.stdout.write(self.style.SUCCESS(f'{number} of {NAME} has been created'))