import datetime
from flask import render_template
from flask import Flask
from BuscaBD import BuscaBD
import json

app = Flask('TESTE')


@app.route("/paciente", methods=["GET"])
def olaMundo():
    con = BuscaBD()
    result = con.buscar_paciente()
    print(result)
    y = json.dumps(con.buscar_paciente(), indent=4,
                   sort_keys=True, default=myconverter)

    # print(y)

    return y


@app.route("/")
@app.route("/index")
def index():
    return render_template('segtela.html')


def myconverter(o):
    return o.__str__()


app.run(debug=True)
