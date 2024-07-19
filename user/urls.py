from django.urls import path
from .views import follow, unfollow, daily_follower_count, common_followers

urlpatterns = [
    path('follow/', follow, name='follow'),
    path('unfollow/', unfollow, name='unfollow'),
    path('follower-count/<int:user_id>/', daily_follower_count, name='daily_follower_count'),
    path('common-followers/<int:user1_id>/<int:user2_id>/', common_followers, name='common_followers'),
]
