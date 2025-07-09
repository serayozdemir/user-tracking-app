# backend/tracking/management/commands/fetch_users.py

from django.core.management.base import BaseCommand
import requests
from tracking.models import User, Address, Company, Geo

class Command(BaseCommand):
    help = 'Fetch users from jsonplaceholder and save to DB'

    def handle(self, *args, **kwargs):
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        users = response.json()

        for u in users:
            geo = Geo.objects.create(
                lat=u["address"]["geo"]["lat"],
                lng=u["address"]["geo"]["lng"]
            )
            address = Address.objects.create(
                street=u["address"]["street"],
                suite=u["address"]["suite"],
                city=u["address"]["city"],
                zipcode=u["address"]["zipcode"],
                geo=geo
            )
            company = Company.objects.create(name=u["company"]["name"])
            user = User.objects.create(
                name=u["name"],
                username=u["username"],
                email=u["email"],
                address=address,
                phone=u["phone"],
                website=u["website"],
                company=company
            )

        self.stdout.write(self.style.SUCCESS('✅ Users fetched and saved successfully!'))
