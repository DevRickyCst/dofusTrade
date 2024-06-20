from django.http import JsonResponse
from itemViewer.models import Item


def get_and_render_all_items_json(request):
    """Retrieve all items according to filter"""
    
    params = request.GET
    print(params)
    items = Item.objects.all()
    
    if 'type' in params:
        if params['type'] == 'Weapon':
            items = items.filter(is_weapon=True)
        else:
            items = items.filter(type__name=params['type'])

    if 'item_name' in params and params['item_name']:
        items = items.filter(name__icontains=params['item_name'])

    if 'lvl_min' in params and params['lvl_min']:
        items = items.filter(level__gte=int(params['lvl_min']))

    if 'lvl_max' in params and params['lvl_max']:
        items = items.filter(level__lte=int(params['lvl_max']))

    if 'page_size' in params and params['page_size']:
        page_size = int(params['page_size'])
        items = items[:page_size]
    else:
        items = items[:20]  # Default page size

    # Using .values() to convert the queryset to a list of dictionaries
    items_list = list(items.values('ankama_id', 'name', 'category', 'type__name', 'description', 'pods', 'level', 'image_urls__icon', 'image_urls__sd'))

    return JsonResponse(items_list, safe=False)