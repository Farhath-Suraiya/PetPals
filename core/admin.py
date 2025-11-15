from django.contrib import admin
from .models import Pet, Favorite

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'is_adopted', 'created_at')
    list_filter = ('is_adopted', 'breed')
    search_fields = ('name', 'breed', 'description')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'created_at')
    search_fields = ('user__username', 'pet__name')
