
from flask import Flask

app = Flask("youtube")


@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return{"ola": "mundo"}


app.run()
