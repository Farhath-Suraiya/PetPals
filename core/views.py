from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Pet, Favorite
from .forms import SignUpForm
from django.contrib import messages

def home(request):
    # show a few latest pets
    latest = Pet.objects.filter(is_adopted=False).order_by('-created_at')[:6]
    return render(request, 'home.html', {'latest': latest})

def pets(request):
    pets_qs = Pet.objects.filter(is_adopted=False).order_by('-created_at')
    return render(request, 'pets.html', {'pets': pets_qs})

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    is_fav = False
    if request.user.is_authenticated:
        is_fav = Favorite.objects.filter(user=request.user, pet=pet).exists()
    return render(request, 'pet_detail.html', {'pet': pet, 'is_fav': is_fav})

@login_required
def add_favorite(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    Favorite.objects.get_or_create(user=request.user, pet=pet)
    messages.success(request, f"Added {pet.name} to favorites.")
    return redirect(request.META.get('HTTP_REFERER', reverse('pets')))

@login_required
def remove_favorite(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    Favorite.objects.filter(user=request.user, pet=pet).delete()
    messages.success(request, f"Removed {pet.name} from favorites.")
    return redirect(request.META.get('HTTP_REFERER', reverse('favorites')))

@login_required
def favorites(request):
    favs = Favorite.objects.filter(user=request.user).select_related('pet').order_by('-created_at')
    pets = [f.pet for f in favs]
    return render(request, 'favorites.html', {'favorites': pets})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login
            login(request, user)
            messages.success(request, "Account created — welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
