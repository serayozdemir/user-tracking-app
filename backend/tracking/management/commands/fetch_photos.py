from django.core.management.base import BaseCommand
import requests
from tracking.models import Photo, Album

class Command(BaseCommand):
    help = 'Fetch photos from jsonplaceholder and save to DB'

    def handle(self, *args, **kwargs):
        photos = requests.get("https://jsonplaceholder.typicode.com/photos").json()
        for p in photos:
            try:
                album = Album.objects.get(id=p["albumId"])
                Photo.objects.create(album=album, title=p["title"], url=p["url"], thumbnail_url=p["thumbnailUrl"])
            except Album.DoesNotExist:
                continue
        self.stdout.write(self.style.SUCCESS("✅ Photos fetched and saved."))