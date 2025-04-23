from django.urls import path
from .views import (
    PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView,
    PhotoCreateView, PhotoUpdateView, PhotoDeleteView, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pets/', PetListView.as_view(), name='pet-list'),
    path('pet/new/', PetCreateView.as_view(), name='pet-create'),
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
    path('pet/<int:pk>/update/', PetUpdateView.as_view(), name='pet-update'),
    path('pet/<int:pk>/delete/', PetDeleteView.as_view(), name='pet-delete'),
    path('pet/<int:pet_id>/photo/new/', PhotoCreateView.as_view(), name='photo-create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo-update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
]