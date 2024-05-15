from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from src.custumRender import render

from .models import CaracteristiqueSetClass, Character, CharacterClass


@login_required
def view_personnages(request, id=None):
    """View to render the character temlate with a specific id or no."""

    # Catch error if id is out of range
    try:
        main_character = Character.objects.get(id=id)
    except:
        main_character = Character.objects.first()

    # Get character associated id
    main_charact_id = main_character.id

    # Get set of carac associated with the character
    carac_set = (
        CaracteristiqueSetClass.objects.filter(character_id=main_charact_id)
        .values(
            "vitalite", "agilite", "chance", "force", "intelligence", "sagesse"
        )
        .first()
    )

    # Other character info in order to render them
    other_charact = (
        Character.objects.filter(user_id=request.user.id)
        .prefetch_related("character_class")
        .values(
            "id", "name", "character_class__name", "character_class__logo_url"
        )
    )

    return render(
        request,
        "perso.html",
        context={
            "character": main_character,
            "other_charact": other_charact,
            "caracteristiques": carac_set,
        },
    )


def update_carac_set(request):
    """Update the caracteristique set using POST methods"""
    if (request.user.is_authenticated) & (request.method == "POST"):
        try:
            # Create user object
            user = User.objects.filter(pk=request.user.id).first()

            # Get character_id from POST value
            character_id = request.POST.get("character_id")

            # Get Characteristique set
            charac_set = CaracteristiqueSetClass.objects.filter(
                character_id=character_id, user=user
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
            return JsonResponse({"200": "Update done"})
        except:
            return JsonResponse({"403": "Pas ok"})


def add_character(request):
    if (request.user.is_authenticated) & (request.method == "POST"):

        user = User.objects.filter(pk=request.user.id).first()

        user_nb_character = Character.objects.filter(user_id=user).count()
        if user_nb_character >= 5:
            return JsonResponse({"404": "not ok"})

        character_class = (
            CharacterClass.objects.first()
        )  # Get the character class by its ID

        if character_class and user:
            try:
                charac = Character(
                    name="New Perso",
                    level=200,
                    server=None,
                    character_class=character_class,
                    user_id=user,
                )

                charac.save()

                characSet = CaracteristiqueSetClass(character_id=charac)

                characSet.save()
                print(charac.id)

                return JsonResponse({"id": charac.id})
            except:
                return JsonResponse({"404": "not ok"})
