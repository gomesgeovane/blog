from django.db import models
from app.account.model import User
from uuid import uuid4

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    id = models.UUIDField(primary_key=True, default=uuid4)
    full_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)

    @property
    def count_following(self):
        return self.following.count()

    @property
    def count_followers(self):
        return self.followers.count()

    def __str__(self):
        return self.full_name