from django.urls import path
from.views import  AnimalCreate, AnimalUpdate, AnimalDelete, AnimalList
from.views import  ProprietarioCreate, ProprietarioUpdate, ProprietarioDelete, ProprietarioList
from.views import  ConsultaCreate, ConsultaDelete, ConsultaList, ConsultaUpdate
from.views import  VeterinarioCreate, VeterinarioDelete, VeterinarioList, VeterinarioUpdate
from .import views
urlpatterns = [

    #Animal

    path('cadastrar/animal', 
    AnimalCreate.as_view(), 
    name='cadastrar-animal'),
    
    path('editar/animal/<int:pk>/',
    AnimalUpdate.as_view(),
    name='editar-animal'),

    path('excluir/animal/<int:pk>/',
    AnimalDelete.as_view(),
    name='excluir-animal'),

    path('listar/animal', 
    views.AnimalList.as_view(), 
    name='listar-animal'),

    #Proprietario

    path('cadastrar/proprietario', 
    ProprietarioCreate.as_view(), 
    name='cadastrar-proprietario'),

    path('editar/proprietario/<int:pk>/',
    ProprietarioUpdate.as_view(),
    name='editar-proprietario'),

    path('excluir/proprietario/<int:pk>/',
    ProprietarioDelete.as_view(),
    name='excluir-proprietario'),

    
    path('listar/proprietario', 
    ProprietarioList.as_view(), 
    name='listar-proprietario'),

    #Consulta Veterinaria
    
    path('marcar/consulta', 
    ConsultaCreate.as_view(), 
    name='marcar-consulta'),

    path('editar/consulta/<int:pk>/',
    ConsultaUpdate.as_view(),
    name='editar-consulta'),

    path('excluir/consulta/<int:pk>/',
    ConsultaDelete.as_view(),
    name='excluir-consulta'),

    path('listar/consulta', 
    ConsultaList.as_view(), 
    name='listar-consulta'),

    #Veterinario

    path('cadastrar/veterinario', 
    VeterinarioCreate.as_view(),
    name='cadastrar-veterinario'),

    path('editar/veterinario/<int:pk>/',
    VeterinarioUpdate.as_view(),
    name='editar-veterinario'),

    path('excluir/veterinario/<int:pk>/',
    VeterinarioDelete.as_view(),
    name='excluir-veterinario'),

    path('listar/veterinario',
    VeterinarioList.as_view(),
    name= 'listar-veterinario'
    )
]