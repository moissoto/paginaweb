from flask import Flask,render_template,request


app = Flask(__name__,template_folder='templates')

@app.route("/", methods=["GET","POST"])
def index()->'html':
    return render_template('index.html',the_title = "Moissoto Web")


@app.route("/calculadora", methods=["GET"])
def calculadora()->'html':
    return render_template("calculadora.html", the_title="Calculadora")

@app.route("/codificador", methods=["GET"])
def codificador () -> 'html':
    return render_template("codificador.html", the_title="Codificador")

@app.route("/recetario", methods=["GET"])
def recetario() -> 'html':
    return render_template ("recetario.html", the_title = "Receetario")

@app.route("/hanging", methods=["GET"])
def hanging () -> 'html':
    return render_template("hanging.html", the_title = "Juego del ahorcado")

@app.route("/compresorzip", methods = ["GET"])
def compresor () -> 'html':
    return render_template("compresorzip.html", the_title="Compresor de archivos a ZIP")

@app.route("/pdftoword", methods = ["GET"])
def pdftotext () -> 'html':
    return render_template("pdftotext.html", the_title="PDF to Word")

@app.route("/mailsender", methods = ["GET"])
def mailsender () -> 'html':
    return render_template("mailsender.html", the_title="Enviar correo")

@app.route("/smssender", methods = ["GET"])
def smssender () -> 'hmtl':
    return render_template ("smssender.html", the_title = 'SMS Sender')

@app.route("/controlhospital", methods=["GET"])
def controlHosital () -> 'html':
    return render_template("controlHospital.html", the_title= "Control Hospital")

@app.route("/controlescolar", methods=["GET"])
def controlEscolar () -> 'html':
    return render_template("controlEscolar.html", the_title = "Control Escolar")

app.run()