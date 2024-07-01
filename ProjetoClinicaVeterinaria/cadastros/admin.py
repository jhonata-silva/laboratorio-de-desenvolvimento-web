from django.contrib import admin

# Register your models here.
from .models import Animal, Proprietario, ConsultaVeterinaria, Veterinario

admin.site.register(Animal)

admin.site.register(Proprietario)

admin.site.register(ConsultaVeterinaria)

admin.site.register(Veterinario)

