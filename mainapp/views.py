from django.http import HttpResponse, JsonResponse
from .models import contacto, ak47, awp, m4a1
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import nuevoContacto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')


def logeo(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html',{
                'form' : AuthenticationForm,
                'error' : 'Usuario o contraseña es incorrecto'
            })
        else:
            login(request, user)
            return redirect('index')
        return render(request, 'login.html',{
            'form' : AuthenticationForm
        })


def registro(request):
    if request.method == 'GET':
        print('enviando formulario')
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    "error": 'usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            "error": 'contraseña no cooincide'
        })
    print(request.POST)
    print('obteniendo datos')

def deslogeo(request):
    logout(request)
    return redirect('index')

#quitar comentario de abajo si se busca redireccionar a login.
#@login_required
def formularioContacto(request):
    if request.method == 'GET':
        return render(request, 'contacto.html', {
            'form': nuevoContacto()
        })
    else:
        contacto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            fecha_creacion=timezone.now()
        )
        return redirect('index')


def ak(request):
    ak47_items = ak47.objects.all()
    return render(request, 'items/ak.html', {'ak47_items': ak47_items})


def awp1(request):
    awp_items = awp.objects.all()
    return render(request, 'items/awp.html', {'awp_items': awp_items})


def m4(request):
    m4a1_items = m4a1.objects.all()
    return render(request, 'items/m4.html', {'m4a1_items': m4a1_items})

def unloged(request):
    return render(request, 'unloged.html')