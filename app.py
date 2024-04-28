from chalice import Chalice, Response
import requests
import os
import jinja2
import dofusdude


configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

api_instance = dofusdude.ConsumablesApi()


app = Chalice(app_name="dofusTrade")

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or      "./")).get_template(filename).render(context)

@app.route("/", methods=["GET"])
def index():
    import json
    val = api_instance.get_all_items_consumables_list(language='en', game='dofus2')

    print(val)


    template = render("chalicelib/templates/base.html", val)
    return Response(template, status_code=200, headers={"Content-Type": "text/html", "Access-Control-Allow-Origin": "*"})