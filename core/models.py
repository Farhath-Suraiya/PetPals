from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pet(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    breed = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)   # simpler: store image URL
    is_adopted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'pet')   # prevent duplicates

    def __str__(self):
        return f"{self.user.username} → {self.pet.name}"
