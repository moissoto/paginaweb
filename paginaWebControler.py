from flask import Flask,render_template,request
from calculadora import operacion
from codificador import encode64,decode64
import base64

app = Flask(__name__,template_folder='templates')

@app.route("/", methods=["GET"])
def index()->'html':
    return render_template('index.html',the_title = "Moissoto Web")


@app.route("/calculadora", methods=["GET","POST"])
def calculadora()->'html':
    if request.method == 'POST':
        n1=int(request.form['n1'])
        n2=int(request.form['n2'])
        op=int(request.form['operacion'])
        data =  operacion(n1,n2,op)
        return render_template("resultado.html", data = data, the_title = 'Resultado')
    else:
        return render_template("calculadora.html", the_title="Calculadora")
        

@app.route("/codificador", methods=["GET","POST"])
def codificador () -> 'html':
    if request.method =='POST':
        texto = request.form['txtarea']
        codificar = request.form['codificar']
        if codificar =='Codificar':
            data = encode64(texto)
        else:
            data = decode64(texto)
        return render_template('codificado.html', data = data, the_title = 'Codigicador')
    else:
        return render_template("codificador.html", the_title="Codificador")

@app.route("/recetario", methods=["GET"])
def recetario() -> 'html':
    return render_template ("recetario.html", the_title = "Recetario")

@app.route("/hangman", methods=["GET"])
def hanging () -> 'html':
    return render_template("hangman.html", the_title = "Juego del ahorcado")

@app.route("/compresorzip", methods = ["GET"])
def compresor () -> 'html':
    return render_template("compresorzip.html", the_title="Compresor de archivos a ZIP")

@app.route("/pdftoword", methods = ["GET"])
def pdftotext () -> 'html':
    return render_template("pdftoword.html", the_title="PDF to Word")

@app.route("/mailsender", methods = ["GET"])
def mailsender () -> 'html':
    return render_template("mailsender.html", the_title="Enviar correo")

@app.route("/smssender", methods = ["GET"])
def smssender () -> 'hmtl':
    return render_template ("smssender.html", the_title = 'SMS Sender')

@app.route("/controlhospital", methods=["GET"])
def controlHosital () -> 'html':
    return render_template("controlhospital.html", the_title= "Control Hospital")

@app.route("/controlescolar", methods=["GET"])
def controlEscolar () -> 'html':
    return render_template("controlescolar.html", the_title = "Control Escolar")

@app.route("/upload", methods = ["GET","POST"])
def upload()->'html':
    if request.method == "POST":
        data = request.method
        return render_template("subirArchivoResultado.html",the_title= "Subir archivo", data=data)
    else:
        return render_template("subirArchivo.html", the_title="Subir Archivo")
        
app.run(debug=True)