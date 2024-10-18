from flask import (Flask , request) #Importa o flask


app= Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) #Assina una rota
def index():
    nome = request.args.get('nome')

    return f"""<h1>Pagina inicial</h1>
     <p>Olá {nome}, que nome bonito!"""


@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galaria</h1>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre</h1>"

@app.route("/area/<float:largura>/<float:comprimento>")
def area(largura: float, comprimento: float):
    return  f"""<h1> A área informada > L={largura}* A={comprimento} =) Area= {largura*comprimento}</h1>"""
@app.route("/parimpar/<float:numero>", methods=('GET',))
def parimpar(numero):
  
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/nome/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomesobrenome(nome, sobrenome):
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/potencia/<float:numero>/<float:elevado>")
def potencia(numero: float, elevado: float):
    return  f"""<h1> A potencia informada > N={numero}* E={elevado} =) Potencia= {numero**elevado}</h1>"""
 
@app.route("/tabuada/<float:n1>", methods=('GET',))
def tabuada(n1: float):

    resultado_tabuada = f"<h2>Tabuada {n1}:</h2>"

    for i in range(11):

        resultado = n1 * i
        resultado_tabuada += f" <ul><li>{n1} x {i} = {resultado}</li></ul>"
    
    return resultado_tabuada




  
