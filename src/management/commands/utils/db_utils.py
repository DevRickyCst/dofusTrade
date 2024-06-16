from itemViewer.models import (
    EffectSingle,
    ImageUrls,
    Item,
    Itemtype,
    Range,
    RecipeSingle,
    Element
)

def insert_item(item, api_type):
    try:
        # Get item type from item (ex: Viande comestible)
        item_type = item.type.to_dict()
        # If item typ doesnt exist create it
        item_type_object, created = Itemtype.objects.get_or_create(
            id=item_type["id"], name=item_type["name"]
        )

        # Get image_urls
        image_urls = item.image_urls.to_dict()
        # Create images_urls
        image_urls_object = ImageUrls.objects.create(
            icon=image_urls["icon"],
            sd=image_urls["sd"],
            hq=image_urls["hq"],
            hd=image_urls["hd"],
        )

        # Get recipe from item
        list_recipe = []
        if item.recipe != None:
            for recip in item.recipe:
                # Create the recipe single
                recipe = RecipeSingle.objects.create(
                    item_ankama_id=recip.item_ankama_id,
                    item_subtype=recip.item_subtype,
                    quantity=recip.quantity,
                )
                list_recipe.append(recipe)

        # Get effects from item
        list_effects = []
        if item.effects != None:
            for _effect in item.effects:
                type, created = Element.objects.get_or_create(
                    id = _effect.type.id,
                    defaults={'name': _effect.type.name}
                )

                # Create the effect single
                effect = EffectSingle.objects.create(
                    int_minimum=_effect.int_minimum,
                    int_maximum=_effect.int_maximum,
                    element = type,
                    ignore_int_min=_effect.ignore_int_min,
                    ignore_int_max=_effect.ignore_int_max,
                    formatted=_effect.formatted,
                )
                list_effects.append(effect)

        items_params = {
            "ankama_id": item.ankama_id,
            "category": api_type,
            "type": item_type_object,
            "name": item.name,
            "description": item.description,
            "level": item.level,
            "pods": item.pods,
            "image_urls": image_urls_object,
        }

        if hasattr(item, "ap_cost"):
            items_params["ap_cost"] = item.ap_cost

        if hasattr(item, "max_cast_per_turn"):
            items_params["max_cast_per_turn"] = item.max_cast_per_turn
        if hasattr(item, "is_weapon"):
            items_params["is_weapon"] = item.is_weapon
        if hasattr(item, "is_two_handed"):
            items_params["is_two_handed"] = item.is_two_handed
        if hasattr(item, "critical_hit_probability"):
            items_params["critical_hit_probability"] = (
                item.critical_hit_probability
            )
        if hasattr(item, "critical_hit_bonus"):
            items_params["critical_hit_bonus"] = item.critical_hit_bonus

        item_object = Item.objects.create(**items_params)
        if hasattr(item, "range"):
            if item.range is not None:
                range = Range.objects.create(
                    item=item_object, max=item.range.min, min=item.range.max
                )

        for _effect in list_effects:
            item_object.effects.add(_effect)
        for _recipe in list_recipe:
            item_object.recipe.add(_recipe)

    except Exception as e:
        raise e
