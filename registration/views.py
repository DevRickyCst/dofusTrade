from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve
from django.http import JsonResponse


def login_view(request):

    if request.method == "POST":
        get_current_route = resolve(request.POST.get("current_page")).route
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            data = {200: "ok"}
            return JsonResponse(
                data
            )  # Redirige vers la page de tableau de bord après la connexion réussie
        else:
            data = {401: "pas ok"}
            return JsonResponse(data)

    return redirect(f"/{get_current_route}")


def logout_view(request):
    logout(request)
    # Redirige vers la page d'accueil ou toute autre page après la déconnexion
    return redirect("/")
