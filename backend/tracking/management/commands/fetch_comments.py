from django.core.management.base import BaseCommand
import requests
from tracking.models import Comment, Post

class Command(BaseCommand):
    help = 'Fetch comments from jsonplaceholder and save to DB'

    def handle(self, *args, **kwargs):
        comments = requests.get("https://jsonplaceholder.typicode.com/comments").json()
        for c in comments:
            try:
                post = Post.objects.get(id=c["postId"])
                Comment.objects.create(post=post, name=c["name"], email=c["email"], body=c["body"])
            except Post.DoesNotExist:
                continue
        self.stdout.write(self.style.SUCCESS("✅ Comments fetched and saved."))