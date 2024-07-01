from django.contrib import admin
from .models import Departamento, Disciplina, Curso, Sala, Horario, HorarioSemana

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Sala)
admin.site.register(Horario)
admin.site.register(HorarioSemana)