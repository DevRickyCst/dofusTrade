import logging

from django.shortcuts import render as django_render

from characterManager.models import Character, CharacterClass

logger = logging.getLogger(__name__)


def render(request, *args, **kwargs):
    args = ("base.html",)

    if request.user.is_authenticated:

        characters = Character.objects.filter(
            user_id=request.user
        ).prefetch_related("character_class")
        # Add the new key-value pair to the inner dictionary
        kwargs["context"]["characteres"] = characters

    # Appelez la fonction render originale avec le contexte mis à jour
    return django_render(request, *args, **kwargs)
