import talisker

# Packages
from canonicalwebteam.flask_base.app import FlaskBase
from flask import render_template
from canonicalwebteam.discourse_docs import DiscourseAPI, DiscourseDocs, DocParser

# Rename your project below
app = FlaskBase(
    __name__,
    "microstack.run",
    template_folder="../templates",
    static_folder="../static",
)

session = talisker.requests.get_session()
doc_parser = DocParser(
    api=DiscourseAPI(base_url="https://discourse.ubuntu.com/", session=session),
        index_topic_id=18212,
        url_prefix="/docs",
    )

if app.debug:
    doc_parser.api.session.adapters["https://"].timeout = 99

discourse_docs = DiscourseDocs(
    parser=doc_parser,
    document_template="docs/document.html",
    url_prefix="/docs",
)
discourse_docs.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")
