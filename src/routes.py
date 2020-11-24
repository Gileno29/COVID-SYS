
from flask import Flask
from BuscaBD import BuscaBD
import json

con = BuscaBD()
con.buscar_paciente()
app = Flask("youtube")


@app.route("/paciente", methods=["GET"])
def olaMundo():
    con = BuscaBD()

    y = json.dumps(con.buscar_paciente(), indent=4, sort_keys=True)

    return y


app.run()
