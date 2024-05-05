from dofusdudes import DofusDudeAPI


interval = [((5 * x) + 1, (5 * x) + 5) for x in range(20)]
full_data = []

for categ in ["equipments", "cosmetics", "resources", "consumables"]:
    for minn, maxx in interval:
        print(minn, maxx)
        api = DofusDudeAPI(categ)
        data = api.get_item_list("fr", "dofus2", lvl_min=minn, lvl_max=maxx)
        for item in data.items:
            full_data.append(item.to_dict())
"""
for data in full_data:
    print(data.update({'categorie':'consumables'}))
    item = Item(**data)
    item.save()"""
