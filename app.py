from chalice import Chalice, Response
import os
import jinja2
import dofusdude



app = Chalice(app_name="dofusTrade")

# Render template with jinja2 templating 
def render(tpl_path, context={}):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or      "./")).get_template(filename).render(context)


@app.route("/", methods=["GET"])
def index():
    template = render("chalicelib/templates/base.html")
    return Response(template, status_code=200, headers={"Content-Type": "text/html", "Access-Control-Allow-Origin": "*"})