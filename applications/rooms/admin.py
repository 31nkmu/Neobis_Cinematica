from django.contrib import admin

from applications.rooms.models import Room, Seat

admin.site.register(Room)
admin.site.register(Seat)