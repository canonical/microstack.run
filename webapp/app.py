import flask
import talisker

# Packages
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam.discourse import (
    DiscourseAPI,
    Docs,
    DocParser,
)

# Rename your project below
app = FlaskBase(
    __name__,
    "microstack.run",
    template_folder="../templates",
    static_folder="../static",
)

session = talisker.requests.get_session()
doc_parser = DocParser(
    api=DiscourseAPI(
        base_url="https://discourse.ubuntu.com/", session=session
    ),
    index_topic_id=18212,
    url_prefix="/docs",
)

if app.debug:
    doc_parser.api.session.adapters["https://"].timeout = 99

discourse_docs = Docs(
    parser=doc_parser,
    document_template="docs/document.html",
    url_prefix="/docs",
)
discourse_docs.init_app(app)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/sitemap.xml")
def sitemap_index():
    xml_sitemap = flask.render_template("sitemap/sitemap-index.xml")
    response = flask.make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response


@app.route("/sitemap-links.xml")
def sitemap_links():
    xml_sitemap = flask.render_template("sitemap/sitemap-links.xml")
    response = flask.make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response
