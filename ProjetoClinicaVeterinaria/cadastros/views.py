
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Animal, Proprietario, ConsultaVeterinaria, Veterinario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
# Create your views here.


class AnimalCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Gerente de Sistema"
    model = Animal
    fields = ['nome', 'especie', 'sexo', 'proprietario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-animal')


class ProprietarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Gerente de Sistema"
    model = Proprietario
    fields = ['nome', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-proprietario')


class AnimalUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Gerente de Sistema"
    model = Animal
    fields = ['nome', 'especie', 'sexo', 'proprietario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-animal')


class ProprietarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Gerente de Sistema"
    model = Proprietario
    fields = ['nome', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-proprietario')


class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-animal')


class ProprietarioDelete(DeleteView):
    model = Proprietario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-proprietario')


#class AnimalList(ListView):
 #   model = Animal
#    template_name = 'cadastros/listas/animal.html'
   
def AnimalList(request):   
    template_name = 'cadastros/listas/animal.html'
    List = Animal.objects.all()
    busca = request.GET.get('seach')
    if busca:
        List = List.filter(nome_icontains = busca)

    return render(request, template_name, List)

class ProprietarioList(LoginRequiredMixin, ListView):
    model = Proprietario
    template_name = 'cadastros/listas/proprietario.html'


class ConsultaCreate(CreateView):
    model = ConsultaVeterinaria
    fields = ['data', 'animal', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-consulta')


class ConsultaUpdate(UpdateView):
    model = ConsultaVeterinaria
    fields = ['data', 'animal', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-consulta')


class ConsultaDelete(DeleteView):
    model = ConsultaVeterinaria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-consulta')


class ConsultaList(LoginRequiredMixin, ListView):
    model = ConsultaVeterinaria
    template_name = 'cadastros/listas/consulta.html'


class VeterinarioCreate(CreateView):
    model = Veterinario
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-veterinarios')


class VeterinarioList(ListView):
    model = Veterinario
    template_name = 'cadastros/listas/veterinario.html'


class VeterinarioUpdate(UpdateView):
    model = Veterinario
    fields = ['nome', 'crmv']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-veterinario')


class VeterinarioDelete(DeleteView):
    model = Veterinario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-veterinario')


class AnimalList(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'cadastros/listas/animal.html'
    login_url = reverse_lazy('login')
