from chalice import Chalice

from chalicelib.blueprints.items_blueprints import items_routes
from chalicelib.utils.jinja2 import return_render_html_file

app = Chalice(app_name="dofusTrade")

app.register_blueprint(items_routes)

@app.route("/", methods=["GET"])
def index():
    return return_render_html_file()



