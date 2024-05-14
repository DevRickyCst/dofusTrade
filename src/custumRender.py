import logging
from django.shortcuts import render as django_render
from characterManager.models import Character

logger = logging.getLogger(__name__)

def render(request, *args, **kwargs):

    context = kwargs.get('context', {})
    template = args[0]

    if request.user.is_authenticated:

        characteres = Character.objects.filter(user_id=request.user).values()
        print(characteres)

        # Add the new key-value pair to the inner dictionary
        kwargs["context"]["characteres"] = characteres


    logger.debug(f"Rendering template : {template} with context #{context}")

    # Appelez la fonction render originale avec le contexte mis à jour
    return django_render(request, *args, **kwargs)