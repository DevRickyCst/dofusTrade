from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from src.custumRender import render

from .models import Character, Set, SetCaracteristique
from itemViewer.models import Item, ItemCategory


def update_carac_set(request):
    """Update the caracteristique set using POST methods"""
    if (request.user.is_authenticated) & (request.method == "POST"):
        try:
            # Get character_id from POST value
            caracteristique_id = request.POST.get("character_id")
            # Get Characteristique set
            charac_set = SetCaracteristique.objects.filter(
                pk=caracteristique_id
            ).first()
            # Update value
            charac_set.vitalite = request.POST.get("vitalite")
            charac_set.agilite = request.POST.get("agilite")
            charac_set.chance = request.POST.get("chance")
            charac_set.force = request.POST.get("force")
            charac_set.intelligence = request.POST.get("intelligence")
            charac_set.sagesse = request.POST.get("sagesse")

            # Save
            charac_set.save()
            return JsonResponse(
                {"message": f"Update done on charac_set {charac_set.id}."},
                status=200,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


def add_character(request):
    if (request.user.is_authenticated) & (request.method == "POST"):

        user = User.objects.filter(pk=request.user.id).first()

        user_nb_character = Character.objects.filter(user_id=user).count()
        if user_nb_character >= 5:
            return JsonResponse(
                {"error": "User cannot have more than 5 characters"},
                status=403,
            )

        if user:
            try:
                charac = Character(
                    name="New Perso",
                    user=user,
                )

                charac.save()
                return JsonResponse({"message": charac.id}, status=201)
            except Exception as e:
                print(e)
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


def delete_character(request):
    """View to delete a character from a character in POST data"""
    if (request.user.is_authenticated) & (request.method == "POST"):
        try:
            # Get user
            user = User.objects.filter(pk=request.user.id).first()
            # Get character_id from POST value
            character_id = request.POST.get("character_id")
            if character_id:
                # Get character
                character = Character.objects.filter(
                    user_id=user, id=character_id
                ).first()
                if character:
                    character.delete()
                    return JsonResponse(
                        {"mesage": f"charac {character_id} has been deleted"},
                        status=200,
                    )
                else:
                    return JsonResponse(
                        {"message": "Character not found"}, status=404
                    )
            else:
                return JsonResponse(
                    {"message": "Invalid character ID"}, status=400
                )
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)
