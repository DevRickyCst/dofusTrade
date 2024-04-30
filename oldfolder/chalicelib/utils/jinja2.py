import jinja2
import os
from typing import Optional
from chalice import Response


def render(
    context: dict = {},
):
    """Render an html fail using jinja2.
    Doc: https://jinja.palletsprojects.com/en/3.1.x/
    """
    # Render index anyway just change the context dict
    path, filename = os.path.split("chalicelib/templates/index.html")
    print(path, filename)
    return (
        jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                path,
                encoding="utf-8",
            )
        )
        .get_template(filename)
        .render(context)
    )


def return_render_html_file(
    context: Optional[dict] = {},
):
    file = render(context=context)
    return Response(
        file,
        status_code=200,
        headers={
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*",
        },
    )
