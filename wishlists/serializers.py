from rest_framework.serializers import ModelSerializer
from rooms.serializers import RoomListSerializer
from .models import Wishlist

class WishlistSerializer(ModelSerializer):

  rooms = RoomListSerializer

  class Meta:
    model = Wishlist
    fields = (
      "name",
      "rooms",
    )