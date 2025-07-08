from django.db import models


from django.db.models import JSONField

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    address = JSONField()  # PostgreSQL'e özel JSON alanı
    phone = models.CharField(max_length=50)
    website = models.URLField()
    company = JSONField()

    class Meta:
        db_table = 'users'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        db_table = 'posts'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

    class Meta:
        db_table = 'comments'

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    class Meta:
        db_table = 'albums'

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    thumbnailUrl = models.URLField()

    class Meta:
        db_table = 'photos'

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'todos'
