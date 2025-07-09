from django.db import models

class Geo(models.Model):
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.lat}, {self.lng}"

class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return f"{self.street}, {self.city}"

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='user')
    phone = models.CharField(max_length=50)
    website = models.URLField()
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f'Comment by {self.name}'

class Album(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=255)
    url = models.URLField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title

class Todo(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title