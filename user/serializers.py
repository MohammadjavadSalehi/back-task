from rest_framework import serializers
from .models import User, Follower


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['user', 'follower', 'followed_at']
