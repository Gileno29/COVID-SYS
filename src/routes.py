import datetime
from flask import Flask
from BuscaBD import BuscaBD
import json

con = BuscaBD()
con.buscar_paciente()
app = Flask("youtube")


@app.route("/paciente", methods=["GET"])
def olaMundo():
    con = BuscaBD()
    result = con.buscar_paciente()
    print(result)
    y = json.dumps(con.buscar_paciente(), indent=4,
                   sort_keys=True, default=myconverter)

    # print(y)

    return y


def myconverter(o):

    return o.__str__()


app.run()
