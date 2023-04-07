from django.shortcuts import render,redirect
from .models import Curso
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages

# Create your views here.

@login_required

def home(request):
    cursosListado=Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListado})

def cerrarSesion(request):
    logout(request)
    return redirect('/')


def register (request):
    form=UserCreationForm(request.POST)
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con éxito')
            return redirect('/')
        else: 
            form=UserCreationForm()  
    context={'form' : form}
    return render(request, 'register.html', context)

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos'] 

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def edicionCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    
    curso=Curso.objects.get(codigo=codigo)

    curso.nombre=nombre
    curso.creditos=creditos
    curso.save()
    return redirect('/')

def eliminarCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')
