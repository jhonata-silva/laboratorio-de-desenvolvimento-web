from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method != 'POST':
        return render(request, 'usuarios/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, passaword=senha)

    if not user:
        messages.error(request, 'usuario ou senha invalido.')
        return render(request, 'usuarios/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'você fez login com sucesso.')
        return redirect('dashboard')


@login_required(redirect_field_name='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
