from src.custumRender import render
from .models import Character
# Create your views here.
def view_personnages(request, id = None):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        try:
            charact = Character.objects.get(id=id)
        except:
            charact = Character.objects.first()
        # Access the user ID
        user_id = request.user.id
        # Print the user ID
        print("User ID:", user_id)
        # Alternatively, you can return the user ID in an HttpResponse
        user_id = request.user.id
    else:
        charact = {}
    charac_type = ['Vitalité','Agilité','Chance','Force','Intelligence','Sagesse']
    return render(request, "perso.html", context = {"character": charact, "charac_type": charac_type})
