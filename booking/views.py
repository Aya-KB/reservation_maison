from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, ReservationForm
from .models import Maison, Client, Reservation
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
def home(request):
    maisons = Maison.objects.all()
    client = None
    reservations = None
    if request.user.is_authenticated:
        try:
            client = Client.objects.get(user=request.user)
            reservations = Reservation.objects.filter(client=client)
        except Client.DoesNotExist:
            client = None
    context = {
        'maisons': maisons,
        'client': client,
        'reservations': reservations,
    }
    return render(request, 'booking/home.html', context) 



def inscription_client(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            nom = form.cleaned_data['nom']

            user = User.objects.create_user(username=email, email=email, password=password)
            # Créer le client lié
            client = Client.objects.create(user=user, nom=nom)
            login(request, user)
            return redirect('liste_maisons')
    else:
        form = UserRegisterForm()
    return render(request, 'booking/inscription.html', {'form': form})

def connexion_client(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)

            # Créer automatiquement un profil client s'il n'existe pas
            Client.objects.get_or_create(user=user, defaults={'nom': user.username})

            return redirect('liste_maisons')
    else:
        form = UserLoginForm()
    return render(request, 'booking/connexion.html', {'form': form})
@login_required
def liste_maisons(request):
    maisons = Maison.objects.all()
    return render(request, 'booking/liste_maisons.html', {'maisons': maisons})



@login_required
def reserver_maison(request, maison_id):
    maison = get_object_or_404(Maison, id=maison_id) 
    try:
        client = request.user.client
    except ObjectDoesNotExist:
        # Créer un client si absent (pour éviter crash)
        client = Client.objects.create(user=request.user, nom=request.user.username)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.client = client
            reservation.maison = maison
            try:
                reservation.save()
                messages.success(request, "Réservation effectuée avec succès !")
                return redirect('espace_client')
            except Exception as e:
                messages.error(request, f"Erreur lors de la réservation : {e}")
        else:
            messages.error(request, "Le formulaire contient des erreurs, veuillez vérifier.")
    else:
        form = ReservationForm()

    return render(request, 'booking/reserver_maison.html', {'form': form, 'maison': maison})

@login_required
def espace_client(request):
    try:
        client = request.user.client
    except ObjectDoesNotExist:
        # Créer un client si absent
        client = Client.objects.create(user=request.user, nom=request.user.username)

    reservations = Reservation.objects.filter(client=client).order_by('-date_debut')
    return render(request, 'booking/espace_client.html', {'client': client, 'reservations': reservations})

def deconnexion_client(request):
    logout(request)
    return redirect('connexion_client')
@login_required
def annuler_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, client__user=request.user)

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Réservation annulée avec succès.")
        return redirect('espace_client')

    return render(request, 'booking/annuler_reservation.html', {'reservation': reservation})
