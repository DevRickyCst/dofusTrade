from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.urls import resolve


def login_view(request):

    if request.method == "POST":
        current_page = request.POST.get("current_page")
        get_current_route = (
            resolve(current_page).route if current_page else "/"
        )

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            data = {"message": "Connexion réussie"}
            return JsonResponse(data, status=200)
        else:
            data = {"error": "Nom d'utilisateur ou mot de passe incorrect"}
            return JsonResponse(data, status=401)

    return HttpResponseRedirect(f"/{get_current_route}")


def logout_view(request):
    logout(request)
    # Redirige vers la page d'accueil ou toute autre page après la déconnexion
    return redirect("/")
