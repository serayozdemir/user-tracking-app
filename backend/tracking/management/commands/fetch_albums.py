from django.core.management.base import BaseCommand
import requests
from tracking.models import Album, User

class Command(BaseCommand):
    help = 'Fetch albums from jsonplaceholder and save to DB'

    def handle(self, *args, **kwargs):
        albums = requests.get("https://jsonplaceholder.typicode.com/albums").json()
        for a in albums:
            try:
                user = User.objects.get(id=a["userId"])
                Album.objects.create(user=user, title=a["title"])
            except User.DoesNotExist:
                continue
        self.stdout.write(self.style.SUCCESS("✅ Albums fetched and saved."))

