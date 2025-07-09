from django.core.management.base import BaseCommand
import requests
from tracking.models import Todo, User

class Command(BaseCommand):
    help = 'Fetch todos from jsonplaceholder and save to DB'

    def handle(self, *args, **kwargs):
        todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
        for t in todos:
            try:
                user = User.objects.get(id=t["userId"])
                Todo.objects.create(user=user, title=t["title"], completed=t["completed"])
            except User.DoesNotExist:
                continue
        self.stdout.write(self.style.SUCCESS("✅ Todos fetched and saved."))
