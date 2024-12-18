from flask import (Flask ,render_template , request) #Importa o flask


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

@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada(numero = None):
   
  if 'numero' in request.args: 
    numero = request.args.get('numero')
    numero = int(request.args.get('numero'))
         
  return render_template('tabuada.html', numero=numero)

@app.route("/juros")
@app.route("/juros/<numero>", methods=("GET", ))
def juros(juros = None , capital= None , tempo= None , deposito= None):
   
  if 'juros'and 'capital' and 'tempo' and 'deposito' in request.args: 
    
    juros = int(request.args.get('juros'))
    capital = int(request.args.get('juros'))
    tempo = int(request.args.get('juros'))
    deposito = int(request.args.get('juros'))
    
         
  return render_template('juros.html', juros=juros , capital=capital , tempo=tempo , deposito=deposito)


@app.route("/login", methods=("GET", ))
def login(email = None , senha= None ):
   
  if 'email'and 'senha' in request.args: 
    
    email = int(request.args.get('email'))
    senha = int(request.args.get('senha'))
   
    
         
  return render_template('login.html', email=email , senha=senha)

@app.route("/imc", methods=("GET",))
def imc(peso = None, altura= None):
  if "peso" and "altura" in request.args:
    peso =float(request.args.get('peso')) 
    altura=float(request.args.get('altura'))
  return render_template("imc.html", peso=peso, altura=altura)







   
 




  
