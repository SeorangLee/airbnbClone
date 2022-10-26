from dataclasses import field
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer

class AmenitySerializer(ModelSerializer):
  class Meta:
    model = Amenity
    fields = (
      "name",
      "description",
    )


class RoomDetailSerializer(ModelSerializer):
  owner = TinyUserSerializer(read_only=True)
  amenities = AmenitySerializer(read_only=True, many=True)
  category = CategorySerializer(read_only=True)
  rating = serializers.SerializerMethodField()
  is_owner = serializers.SerializerMethodField()
  photos = PhotoSerializer(many = True, read_only = True)

  class Meta:
    model = Room
    fields = "__all__"
  
  def create(self, validated_data):
      return Room.objects.create(**validated_data)
  
  def get_rating(self, room): #이름은 꼭 이렇게 지어줘야함(serializer Method filed 규칙)
    return room.rating()

  def get_is_owner(self, room):
    request = self.context['request']
    return room.owner == request.user 


class RoomListSerializer(ModelSerializer):

  rating = serializers.SerializerMethodField()
  is_owner = serializers.SerializerMethodField()
  photos = PhotoSerializer(many = True, read_only = True)

  class Meta:
    model = Room
    fields = (
      "pk",
      "name",
      "country",
      "city",
      "price",
      "rating",
      "is_owner",
      "photos",
    )

  def get_rating(self, room):
    return room.rating()
  
  def get_is_owner(self, room):
    request = self.context['request']
    return room.owner == request.user

