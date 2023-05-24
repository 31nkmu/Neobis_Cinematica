from django.contrib import admin

from applications.movies.models import Movie, ShowTime

admin.site.register(Movie)
admin.site.register(ShowTime)
