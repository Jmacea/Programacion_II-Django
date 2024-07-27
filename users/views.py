from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from .forms import LoginForm, UserEditForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from users.models import User

# Create your views here.

# Manejando los errores
def error_403(request, exception):
    return render(request, 'error_403.html')

# Login
def login_user(request):
    # validacion con methodo Post
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            # validando si es un usuario o no
            if user is not None :
                login(request, user)
            else:
                messages.error(request, "Usuario No Registrado")
                return JsonResponse({'result': 'not register', 'status1': 'usuario no registrado'})
        else:
            # manejando los errores en formato Json
            errors = form.errors
            return JsonResponse({'result': 'error', 'errors': errors})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Registro
def register(request):
    if request.method == 'POST':
        # en este caso validamos el formulario y los archvios que se carguen
        
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'good', 'mensaje': 'Usuario Creado Satisfactoriamente'})
        else:
            errors = form.errors
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        form = UserForm()
    return render(request, 'registro.html', {'form': form})

# cerrar sesion
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def exit(request):
    logout(request)
    return redirect('login_user')

# listado de usuario
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def list_users(request):
    # se crea un diccionarion donde el parametro users realiza una consulta con el orm de django
    users = {
        'users': User.objects.all(),
        'title': 'Usuarios'
    }
    return render(request, 'users/users.html', users)

@permission_required('auth.user_view',login_url="/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        # en este caso validamos el formulario y los archvios que se carguen
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid(): #validamos en formulario
            # se maneja la respuesta en formato JSOn
            user = form.save()
            return JsonResponse({'status': 'good', 'mensaje': 'Usuario Editado Satisfactoriamente'})
        else:    
            # se maneja la respuesta en formato JSOn
            errors = form.errors
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        form = UserEditForm(instance=user)
    return render(request, 'users/edit.html', {'form': form, 'user': user})

@permission_required('auth.user_view',login_url="/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Informacion Eliminada satisfastoriamente')
        return redirect('list_users')
    return render(request, 'users/delete.html', {'user': user})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def edit_perfil(request):
    if request.method == 'POST':
        # en este caso validamos el formulario y los archvios que se carguen
        
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid(): #validamos en formulario
            form.save()
            # se maneja la respuesta en formato JSOn
            return JsonResponse({'status': 'good', 'mensaje': 'Usuario Editado Satisfactoriamente'})
        else:
            errors = form.errors
            # se maneja la respuesta en formato JSOn
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'users/perfil.html', {'form': form}) 

@permission_required('auth.user_view',login_url="/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_admin(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid(): #validamos en formulario
            admin = form.save(commit=False)
            admin.is_superuser = True
            admin.save()
            # se maneja la respuesta en formato JSOn
            return JsonResponse({'status': 'good', 'mensaje': 'Usuario Creado Satisfactoriamente'})
        else:
            errors = form.errors
            # se maneja la respuesta en formato JSOn
            return JsonResponse({'result': 'error', 'errors': errors})
    else:
        form = UserForm()
    return render(request, 'users/useradmin.html', {'form': form}) 