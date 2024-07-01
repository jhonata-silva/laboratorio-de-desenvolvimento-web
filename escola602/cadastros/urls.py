from django.urls import path
from .views import DepartamentoCreate, DisciplinaCreate, CursoCreate, SalaCreate
from .views import DepartamentoUpdade, DisciplinaUpdate, CursoUpdate, SalaUpdate
from .views import DepartamentoDelete, DisciplinaDelete, CursoDelete, SalaDelete
from .views import DepartamentoList, DisciplinaList, CursoList, SalaList

urlpatterns = [

    path(
        'cadastrar/departamento/',
        DepartamentoCreate.as_view(),
        name='cadastrar-departamento'
    ),
    path(
        'cadastrar/disciplina/',
        DisciplinaCreate.as_view(),
        name='cadastrar-disciplina'
    ),
    path(
        'cadastrar/curso/',
        CursoCreate.as_view(),
        name='cadastrar-curso'
    ),
    path(
        'cadastrar/sala/',
        SalaCreate.as_view(),
        name='cadastrar-sala'
    ),
    path(
        'editar/departamento/<int:pk>/',
        DepartamentoUpdade.as_view(),
        name='editar-departamento'
    ),
    path(
        'editar/disciplina/<int:pk>/',
        DisciplinaUpdate.as_view(),
        name='editar-disciplina'
    ),
    path(
        'editar/curso/<int:pk>/',
        CursoUpdate.as_view(),
        name='editar-curso'
    ),
    path(
        'editar/sala/<int:pk>/',
        SalaUpdate.as_view(),
        name='editar-sala'
    ),
    path(
        'excluir/departamento/<int:pk>/',
        DepartamentoDelete.as_view(),
        name='excluir-departamento'
    ),
    path(
        'excluir/disciplina/<int:pk>/',
        DisciplinaDelete.as_view(),
        name='excluir-disciplina'
    ),
    path(
        'excluir/curso/<int:pk>/',
        CursoDelete.as_view(),
        name='excluir-curso'
    ),
    path(
        'excluir/sala/<int:pk>/',
        SalaDelete.as_view(),
        name='excluir-sala'
    ),
    path(
        'listar/departamento/',
        DepartamentoList.as_view(),
        name='listar-departamento'
    ),
     path(
        'listar/disciplina/',
        DisciplinaList.as_view(),
        name='listar-disciplina'
    ),
    path(
        'listar/curso/',
        CursoList.as_view(),
        name='listar-curso'
    ),
    path(
        'listar/sala/',
        SalaList.as_view(),
        name='listar-sala'
    ),
]