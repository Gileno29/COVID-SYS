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
    dados = f.calculaMorteSexo()
    print(dados)

    return render_template('segtela.html', mulher=dados['mulher'],
                           homem=dados['homem'])


def myconverter(o):
    return o.__str__()


app.run(debug=True, port=4000)
