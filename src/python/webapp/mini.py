import flask as f

from webapp.anotherpkg import MESSAGE
app = f.Flask(__name__)

@app.route("/")
def hello():
    return f.render_template("index.html", message=MESSAGE)

def run():
    app.run()

if __name__ == "__main__":
    run()
