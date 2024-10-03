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