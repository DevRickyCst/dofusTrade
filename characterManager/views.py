from src.custumRender import render
from .models import Character, CaracteristiqueSetClass, CharacterClass
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


def view_personnages(request, id = None):

    if request.user.is_authenticated:
        try:
            main_charact = Character.objects.get(id=id)
        except:
            main_charact = Character.objects.first()
        
        main_charact_id = main_charact.id
        #Get other charact for menu selection
        other_charact = (Character.objects
                         .filter(user_id= request.user.id)
                         .prefetch_related('character_class')
                         .values('id', 'name', 'character_class__name', 'character_class__logo_url'))
        
        caracteristiques = (CaracteristiqueSetClass.objects
                            .filter(character_id= main_charact_id)
                            .values('vitalite', 'agilite', 'chance', 
                                   'force', 'intelligence', 'sagesse')
                            .first())
        
    else:
        main_charact = {}

    return render(request, "perso.html", context = {"character": main_charact, 
                                                    'other_charact': other_charact,
                                                    'caracteristiques': caracteristiques})


def update_carac_set(request):
    print(request.POST)
    if (request.user.is_authenticated) & (request.method == "POST"):
        vitalite = request.POST.get("vitalite")
        agilite = request.POST.get("agilite")
        chance = request.POST.get("chance")
        force = request.POST.get("force")
        intelligence = request.POST.get("intelligence")
        sagesse = request.POST.get("sagesse")

        character_id = request.POST.get("character_id")

        charac_set = (CaracteristiqueSetClass.objects
                      .filter(character_id=character_id)
                      .first())

        charac_set.vitalite = vitalite
        charac_set.agilite = agilite
        charac_set.chance = chance
        charac_set.force = force
        charac_set.intelligence = intelligence
        charac_set.sagesse = sagesse
        try:
            charac_set.save()
            return JsonResponse({
                '200': 'Update done'
            })
        except:
            return JsonResponse({
                '403': 'Pas ok'
            })
        
def add_character(request):
    if (request.user.is_authenticated) & (request.method == "POST"):

        user = User.objects.filter(pk=request.user.id).first()

        user_nb_character = Character.objects.filter(user_id=user).count()

        print(user_nb_character)
        if user_nb_character >= 5:
            return JsonResponse({'404': 'not ok'})
        character_class = CharacterClass.objects.filter(pk=1).first()  # Get the character class by its ID

        print(character_class)
        if character_class and user:
            charac = Character(
                name = 'New Perso',
                level = 200,
                server = 'test',
                character_class = character_class,
                user_id = user
            )

            charac.save()

            characSet = CaracteristiqueSetClass(
                character_id = charac
            )

            characSet.save()
            print(charac.id)
    
            return JsonResponse({'id':charac.id})

