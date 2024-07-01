from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Departamento, Disciplina, Curso, Sala
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Views de Criação (CreateView)
class DepartamentoCreate(LoginRequiredMixin, CreateView):
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

class DisciplinaCreate(LoginRequiredMixin, CreateView):
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplina')
    login_url = reverse_lazy('login')

class CursoCreate(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ['nome', 'modalidade', 'departamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-curso')
    login_url = reverse_lazy('login')

class SalaCreate(LoginRequiredMixin, CreateView):
    model = Sala
    fields = ['nome', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-sala')
    login_url = reverse_lazy('login')

# Views de atualização (UpdateView)
class DepartamentoUpdade(LoginRequiredMixin, UpdateView):
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplina')
    login_url = reverse_lazy('login')

class CursoUpdate(LoginRequiredMixin, UpdateView):
    model = Curso
    fields = ['nome', 'modalidade', 'departamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-curso')
    login_url = reverse_lazy('login')

class SalaUpdate(LoginRequiredMixin, UpdateView):
    model = Sala
    fields = ['nome', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-sala')
    login_url = reverse_lazy('login')

#views de exclusão (DeleleView)
class DepartamentoDelete(LoginRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

class DisciplinaDelete(LoginRequiredMixin, DeleteView):
    model = Disciplina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-disciplina')
    login_url = reverse_lazy('login')

class CursoDelete(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-curso')
    login_url = reverse_lazy('login')

class SalaDelete(LoginRequiredMixin, DeleteView):
    model = Sala
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-sala')
    login_url = reverse_lazy('login')

# Views de listagem (ListView)
class DepartamentoList(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = 'cadastros/listas/departamento.html'
    login_url = reverse_lazy('login')

class DisciplinaList(LoginRequiredMixin, ListView):
    model = Disciplina
    template_name = 'cadastros/listas/disciplina.html'
    login_url = reverse_lazy('login')

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cadastros/listas/curso.html'
    login_url = reverse_lazy('login')

class SalaList(LoginRequiredMixin, ListView):
    model = Sala
    template_name = 'cadastros/listas/sala.html'
    login_url = reverse_lazy('login')