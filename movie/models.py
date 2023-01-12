# from django.db import models

# # Create your models here.

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    actors = models.ManyToManyField("movie.Actor")
    director = models.ForeignKey("movie.Director", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        return self.ratings.aggregate(Avg("value"))["value__avg"]

    @property
    def ratings_count(self):
        return self.ratings.count()


class Rating(models.Model):
    value = models.PositiveIntegerField()
    movie = models.ForeignKey("movie.Movie", on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating for {self.movie.name}: {self.value}"

