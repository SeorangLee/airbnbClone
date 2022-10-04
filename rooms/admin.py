from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

  #모델 속성 뿐만 아니라 메소드도 작성 가능
  list_display = (
    "name",
    "price",
    "kind",
    "total_amenities",
    "rating",
    "owner",
    "created_at",
  )

  list_filter = (
    "country",
    "city",
    "price",
    "rooms",
    "toilets",
    "pet_friendly",
    "kind",
    "amenities",
    "created_at",
    "updated_at",
  )

  search_fields = (
    "owner__username",
  )

  # def total_amenities(self, room):
  #   return room.amenities.count()

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
  list_display = (
    "name",
    "description",
    "created_at",
    "updated_at",
  )

  readonly_fields = (
    "created_at",
    "updated_at",
  )