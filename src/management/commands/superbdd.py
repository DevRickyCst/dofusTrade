import dofusdude
import dofusdude.api_client
from dofusdude.rest import ApiException
from pprint import pprint
from datetime import date
import requests
import json
from itemViewer.models import Item
from django.core.management.base import BaseCommand, CommandError

# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
class Command(BaseCommand):
    help = "Fill Bdd with consumables"

    def add_arguments(self, parser):
        #nothing
        print()

    def handle(self, *args, **options):

        configuration = dofusdude.Configuration(
        host = "https://api.dofusdu.de"
        )

        #Flushing previous entries in db
        all_bdd_items = Item.objects.all()
        deleted_items_count = 0
        added_items_count = 0
        print("Found " + all_bdd_items.count().__str__() + " entries in db")
        if all_bdd_items.count() != 0:
            for bdd_item in all_bdd_items:
                bdd_item.delete()
                deleted_items_count += 1
        print("Deleted " + deleted_items_count.__str__() + " entries in db")

        with dofusdude.ApiClient(configuration) as api_client:
        # Create an instance of the API class
            api_instance = dofusdude.ConsumablesApi(api_client)
            language = 'fr' # str | a valid language code
            game = 'dofus2' # str | 
            sort_level = 'asc' # str | sort the resulting list by level, default unsorted (optional)

            page_size = -1 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
            page_number = 1 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)

            try:
                # Consumables endpoint
                api_response = api_instance.get_items_consumables_list(language, game, sort_level=sort_level, page_size=page_size, page_number=page_number).to_json()
                json_response = json.loads(api_response)
                print("The response of ConsumablesApi->get_items_consumables_list: " + len(json_response["items"]).__str__() + " consumables\n")
                for item in json_response['items'] :
                    i = Item(ankama_id= item['ankama_id'], name=['name'])
                    i.type = item['type']['name']
                    i.level = item['level']
                    i.image_urls = item['image_urls']
                    i.categorie = "consumables"
                    i.save()
                    added_items_count += 1
                print("Added " + added_items_count.__str__() + " entries to db")
            except Exception as e:
                print("Exception when calling ConsumablesApi->get_items_consumables_list: %s\n" % e)





















    """
# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
# Create an instance of the API class
api_instance = dofusdude.AlmanaxApi(api_client)
language = 'fr' # str | code
var_date = date.today() # date | yyyy-mm-dd

try:
    # Single Almanax Date
    api_response = api_instance.get_almanax_date(language, var_date)
    print("The response of AlmanaxApi->get_almanax_date:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlmanaxApi->get_almanax_date: %s\n" % e)
"""

"""payload = {'page_size': '10', 'filter_max_level' : 2}
#r = requests.get('https://api.dofusdu.de/dofus2/fr/items/consumables/', params=payload)
r = requests.get('https://api.dofusdu.de/dofus2/fr/items/consumables?page-number=1&page-size=16')

print(r.status_code)
jsonResponse = json.loads(r.content)
jsonReadable = json.dumps(jsonResponse, indent=2)
print(len(jsonResponse["items"][0]))
print(jsonReadable)"""
