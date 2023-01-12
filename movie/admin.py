# from django.contrib import admin

# # Register your models here.

from django.contrib import admin

from movie.models import Actor, Director, Movie, Rating


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = [
        "average_rating",
        "ratings_count",
        "created_at",
        "updated_at"
    ]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
