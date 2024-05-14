import logging
from django.shortcuts import render as django_render

logger = logging.getLogger(__name__)

def render(request, *args, **kwargs):

    context = kwargs.get('context', {})
    template = args[0]

    logger.debug(f"Rendering template : {template} with context #{context}")

    # Appelez la fonction render originale avec le contexte mis à jour
    return django_render(request, *args, **kwargs)