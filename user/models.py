from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username


class Follower(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'follower')

    def __str__(self):
        return f'{self.follower} follows {self.user}'
