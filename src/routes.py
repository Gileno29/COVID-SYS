from flask import render_template
from flask import Flask
from Filtro import Filtro


app = Flask(__name__)

''''
@app.route("/paciente", methods=["GET"])
def olaMundo():
    con = BuscaBD()
    result = con.buscar_paciente()
    print(result)
    y = json.dumps(con.buscar_paciente(), indent=4,
                   sort_keys=True, default=myconverter)

    # print(y)

    return y
'''


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


def dados_estado():
    pass


def myconverter(o):
    return o.__str__()


app.run(debug=True, port=4000)
