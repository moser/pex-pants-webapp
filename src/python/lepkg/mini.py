from flask import Flask

from lepkg.anotherpkg import MESSAGE
app = Flask(__name__)

@app.route("/")
def hello():
    return MESSAGE

def run():
    app.run()

if __name__ == "__main__":
    run()
