from django.contrib import admin
from .models import Pet, PetPhoto

class PetPhotoInline(admin.TabularInline):
    model = PetPhoto
    extra = 1

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_type', 'owner')
    inlines = [PetPhotoInline]

@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('pet', 'date', 'caption')
    list_filter = ('pet', 'date')