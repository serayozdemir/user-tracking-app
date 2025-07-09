from django.core.management.base import BaseCommand
import requests
from tracking.models import Post, User

class Command(BaseCommand):
    help = 'Fetch posts from jsonplaceholder and save to DB'

    def handle(self, *args, **kwargs):
        posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
        for p in posts:
            try:
                user = User.objects.get(id=p["userId"])
                Post.objects.create(user=user, title=p["title"], body=p["body"])
            except User.DoesNotExist:
                continue
        self.stdout.write(self.style.SUCCESS("✅ Posts fetched and saved."))
