from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Pet, PetPhoto

class HomeView(TemplateView):
    template_name = 'pets/home.html'

class PetListView(ListView):
    model = Pet
    template_name = 'pets/pet_list.html'

class PetDetailView(DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'

class PetCreateView(CreateView):
    model = Pet
    fields = ['name', 'pet_type', 'breed', 'birth_date']
    template_name = 'pets/pet_form.html'
    success_url = reverse_lazy('pet-list')

class PetUpdateView(UpdateView):
    model = Pet
    fields = ['name', 'pet_type', 'breed', 'birth_date']
    template_name = 'pets/pet_form.html'
    
    def get_success_url(self):
        return reverse_lazy('pet-detail', kwargs={'pk': self.object.pk})

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pets/pet_confirm_delete.html'
    success_url = reverse_lazy('pet-list')

class PhotoCreateView(CreateView):
    model = PetPhoto
    fields = ['image', 'caption', 'date']
    template_name = 'pets/photo_form.html'
    
    def form_valid(self, form):
        form.instance.pet = Pet.objects.get(pk=self.kwargs['pet_id'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('pet-detail', kwargs={'pk': self.kwargs['pet_id']})

class PhotoUpdateView(UpdateView):
    model = PetPhoto
    fields = ['image', 'caption', 'date']
    template_name = 'pets/photo_form.html'
    
    def get_success_url(self):
        return reverse_lazy('pet-detail', kwargs={'pk': self.object.pet.pk})

class PhotoDeleteView(DeleteView):
    model = PetPhoto
    template_name = 'pets/photo_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('pet-detail', kwargs={'pk': self.object.pet.pk})