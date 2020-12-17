from flask import render_template
from flask import Flask
from flask import request
from flask import redirect
from Filtro import Filtro
from BuscaBD import BuscaBD
import json


app = Flask(__name__)

user = ''


@app.route("/paciente", methods=["GET"])
def olaMundo():
    con = BuscaBD()
    #result = con.buscar_paciente()
    # print(result)
    y = json.dumps(con.buscar_paciente(), indent=4,
                   sort_keys=True, default=myconverter)

    return y


@app.route("/dados")
def index():
    f = Filtro()
    dados_sexo = f.calcula_morte_sexo()
    dados_sintomas = f.calcula_morte_sintomas()
    dados_idade = f.calcular_morte_por_idade()
    dados_por_mes = f.quantidade_obtos_mes()
    print("dados por mes", dados_por_mes)
    return render_template('segtela.html', mulher=dados_sexo['mulher'], homem=dados_sexo['homem'],
                           febre=dados_sintomas['febre'], dor_garganta=dados_sintomas['dor_garganta'],
                           tosse=dados_sintomas['tosse'], dispineia=dados_sintomas['dispineia'],
                           outros=dados_sintomas['outros'], idade0A25=dados_idade['idade0A25'],
                           idade26A30=dados_idade['idade26A30'], idade31A40=dados_idade['idade31A40'],
                           idade41A60=dados_idade['idade41A60'], maisDe60=dados_idade[
        'maisDe60'], janeiro=dados_por_mes['janeiro'], fevereiro=dados_por_mes['fevereiro'],
        marco=dados_por_mes['marco'], abril=dados_por_mes['abril'], maio=dados_por_mes['maio'],
        junho=dados_por_mes['junho'], julho=dados_por_mes['julho'], agosto=dados_por_mes['agosto'],
        setembro=dados_por_mes['setembro'], outubro=dados_por_mes['outubro'],
        novembro=dados_por_mes['novembro'], dezembro=dados_por_mes['dezembro'])


@app.route("/busca-estado", methods=["GET", "POST"])
def dados_estado():

    if request.method == 'POST':
        estado = request.form['estado']

        f = Filtro()
        dados_sexo = f.calcula_morte_sexo(estado)
        dados_sintomas = f.calcula_morte_sintomas(estado)
        dados_idade = f.calcular_morte_por_idade(estado)
        dados_por_mes = f.quantidade_obtos_mes(estado)
        print("dados por mes", dados_por_mes)
        return render_template('segtela.html', mulher=dados_sexo['mulher'], homem=dados_sexo['homem'],
                               febre=dados_sintomas['febre'], dor_garganta=dados_sintomas['dor_garganta'],
                               tosse=dados_sintomas['tosse'], dispineia=dados_sintomas['dispineia'],
                               outros=dados_sintomas['outros'], idade0A25=dados_idade['idade0A25'],
                               idade26A30=dados_idade['idade26A30'], idade31A40=dados_idade['idade31A40'],
                               idade41A60=dados_idade['idade41A60'], maisDe60=dados_idade[
                                   'maisDe60'], janeiro=dados_por_mes['janeiro'], fevereiro=dados_por_mes['fevereiro'],
                               marco=dados_por_mes['marco'], abril=dados_por_mes['abril'], maio=dados_por_mes['maio'],
                               junho=dados_por_mes['junho'], julho=dados_por_mes['julho'], agosto=dados_por_mes['agosto'],
                               setembro=dados_por_mes['setembro'], outubro=dados_por_mes['outubro'],
                               novembro=dados_por_mes['novembro'], dezembro=dados_por_mes['dezembro'])

    # return render_template('apreensaoForm.html', titulo='Nova Apreensao')
    else:
        return 'METHOD POST DONT EXIST'


@app.route("/logado", methods=["GET", "POST"])
def logado():
    if request.method == 'POST':
        global user
        user = request.form['imagem']

    return redirect("/dados")


@app.route("/")
@app.route("/login")
def login():
    return render_template('index.html')


@app.route("/deslogado",  methods=["GET", "POST"])
def deslogado():
    return redirect('/login')


def myconverter(o):
    return o.__str__()


app.run(debug=True, port=4000)
