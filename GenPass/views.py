from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .forms import *
from .utils import generate_password
from django.shortcuts import render, get_object_or_404

# db
from django.db import IntegrityError

# User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def error_404_view(request, exception):
    return render(request, "404.html")


## Static page
def servicios(request):
    return render(request, "servicios.html")


def myfunctioncall(request):
    return render(request, "index.html")


## Main proyect
def gp(request):
    length = int(request.GET.get("length", 16))
    include_uppercase = request.GET.get("uppercase"), True
    include_numbers = request.GET.get("numbers"), True
    password = generate_password(length, include_uppercase, include_numbers)
    mydictionary = {"password": password}
    return render(request, "index.html", context=mydictionary)


## Registro
def registro(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Validar que la contraseña coincida con la confirmación de la contraseña
        if password != confirm_password:
            return render(
                request, "registro.html", {"error": "Las contraseñas no coinciden"}
            )

        # Crear un nuevo usuario
        try:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            user.save()
        except IntegrityError:
            return render(
                request,
                "registro.html",
                {"error": "El correo electrónico ya está registrado"},
            )

        # Autenticar y hacer login del nuevo usuario
        new_user = authenticate(username=username, password=password)
        login(request, new_user)

        return redirect("/")
    else:
        return render(request, "user/registro.html")


## Login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "user/login.html", {"error": "Invalid credentials"})
    else:
        return render(request, "user/login.html")


## Logout
def logout_view(request):
    logout(request)
    return redirect("index")


def myfunctionabout(request):
    return HttpResponse("About Response")


def add(request, a, b):
    return HttpResponse(a + b)


def intro(request, name, age):
    mydictionary = {"name": name, "age": age}
    return JsonResponse(mydictionary)


def myimagepage5(request, imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var = True
    elif myimagename == "python":
        var = False
    mydictionary = {"var": var}
    return render(request, "imagepage5.html", context=mydictionary)


# View Profile Page (User) and Other Users


def profile(request, username):
    if request.user.username == username:
        # si se está accediendo al perfil propio
        user = request.user
    else:
        # si se está accediendo al perfil de otro usuario
        user = get_object_or_404(User, username=username)

    context = {"user": user}
    return render(request, "user/profile.html", context)
