from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # page d'accueil
    path('inscription_client/', views.inscription_client, name='inscription_client'),
    path('connexion/', views.connexion_client, name='connexion_client'),
    path('deconnexion/', views.deconnexion_client, name='deconnexion_client'),  
    path('liste_maisons/', views.liste_maisons, name='liste_maisons'),
    path('reserver_maison/<int:maison_id>/', views.reserver_maison, name='reserver_maison'),
    path('espace_client/', views.espace_client, name='espace_client'),
    path('reservation/<int:reservation_id>/annuler/', views.annuler_reservation, name='annuler_reservation'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)