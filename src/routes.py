from flask import render_template
from flask import Flask
from flask import request
from flask import redirect
from Filtro import Filtro
from BuscaBD import BuscaBD
import json


app = Flask(__name__)


@app.route("/paciente", methods=["GET"])
def olaMundo():
    con = BuscaBD()
    #result = con.buscar_paciente()
    # print(result)
    y = json.dumps(con.buscar_paciente(), indent=4,
                   sort_keys=True, default=myconverter)

    return y


@app.route("/")
@app.route("/dados")
def index():
    f = Filtro()
    dados_sexo = f.calcula_morte_sexo()
    dados_sintomas = f.calcula_morte_sintomas()
    print(dados_sintomas)

    return render_template('segtela.html', mulher=dados_sexo['mulher'],
                           homem=dados_sexo['homem'], febre=dados_sintomas['febre'], dor_garganta=dados_sintomas['dor_garganta'],
                           tosse=dados_sintomas['tosse'], dispineia=dados_sintomas['dispineia'],
                           outros=dados_sintomas['outros'])


@app.route("/busca-estado", methods=["GET", "POST"])
def dados_estado():

    if request.method == 'POST':
        estado = request.form['estado']

        f = Filtro()
        dados_sexo = f.calcula_morte_sexo(estado)
        dados_sintomas = f.calcula_morte_sintomas(estado)
        dados_idade = f.calcula_morte_por_idade(estado)
        return render_template('segtela.html', mulher=dados_sexo['mulher'], homem=dados_sexo['homem'],
                               febre=dados_sintomas['febre'], dor_garganta=dados_sintomas['dor_garganta'],
                               tosse=dados_sintomas['tosse'], dispineia=dados_sintomas['dispineia'],
                               outros=dados_sintomas['outros'], idade0A25=dados_idade['idade0A25'],
                               idade26A30=dados_idade['idade26A30'], idade31A40=dados_idade['idade31A40'],
                               idade41A60=dados_idade['idade41A60'], maisDe60=dados_idade['maisDe60'])

    # return render_template('apreensaoForm.html', titulo='Nova Apreensao')
    else:
        return 'METHOD POST DONT EXIST'


@app.route("/login")
def login():
    return render_template('index.html')


def myconverter(o):
    return o.__str__()


app.run(debug=True, port=4000)
