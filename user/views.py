from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Follower
from .serializers import UserSerializer, FollowerSerializer
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta


@api_view(['POST'])
def follow(request):
    user_id = request.data.get('user_id')
    follower_id = request.data.get('follower_id')
    user = get_object_or_404(User, id=user_id)
    follower = get_object_or_404(User, id=follower_id)

    if Follower.objects.filter(user=user, follower=follower).exists():
        return Response({"detail": "Already following"}, status=status.HTTP_400_BAD_REQUEST)

    Follower.objects.create(user=user, follower=follower)
    return Response({"detail": "Followed successfully"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def unfollow(request):
    user_id = request.data.get('user_id')
    follower_id = request.data.get('follower_id')
    user = get_object_or_404(User, id=user_id)
    follower = get_object_or_404(User, id=follower_id)

    follower_relation = Follower.objects.filter(user=user, follower=follower).first()
    if follower_relation:
        follower_relation.delete()
        return Response({"detail": "Unfollowed successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Not following"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def daily_follower_count(request, user_id):
    user = get_object_or_404(User, id=user_id)
    start_date = timezone.now() - timedelta(days=1)
    follower_count = Follower.objects.filter(user=user, followed_at__gte=start_date).count()
    return Response({"user_id": user.id, "username": user.username, "follower_count": follower_count})


@api_view(['GET'])
def common_followers(request, user1_id, user2_id):
    user1 = get_object_or_404(User, id=user1_id)
    user2 = get_object_or_404(User, id=user2_id)

    user1_followers = set(user1.followers.values_list('follower_id', flat=True))
    user2_followers = set(user2.followers.values_list('follower_id', flat=True))

    common_follower_ids = user1_followers.intersection(user2_followers)
    common_followers = User.objects.filter(id__in=common_follower_ids)

    serializer = UserSerializer(common_followers, many=True)
    return Response(serializer.data)
