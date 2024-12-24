from flask import Flask,render_template,request
from calculadora import operacion
from codificador import encode64,decode64
import gzip, shutil
from pdf2docx import Converter
import smtplib
from email.message import EmailMessage


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

@app.route("/agendaTelefonica", methods=["GET","POST"])
def agendaTelefonica() ->'html':
    if request.method=='POST':
        nombre = request.form['nombre']
        pseudonimo = request.form['pseudonimo']
        telefono = request.form['telefono']
        email = request.form['correo']
        agenda = {
            'Nombre':nombre,
            'Pseudonimo': pseudonimo,
            'Teléfono':telefono,
            'Email':email
        }
        return render_template('mostrarAgenda.html',the_title='Agenda Telefónica', agenda = agenda)
    else:
        return render_template("agenda.html",the_title='Agenda Telefónica')

@app.route("/recetario", methods=["GET","POST"])
def recetario() -> 'html':
    if request.method=="POST":
        titulo = request.form['titulo']
        descripcion= request.form['descripcion']
        ingredientes = request.form['ingredientes']
        preparacion = request.form['preparacion']
        receta = {
            'titulo' : titulo,
            'descripcion' : descripcion,
            'ingredientes' : ingredientes,
            'preparacion' : preparacion
        }
        return render_template ('mostrarReceta.html', the_title = 'Recetario', receta = receta)

    return render_template ("recetario.html", the_title = "Recetario")

@app.route("/hangman", methods=["GET"])
def hanging () -> 'html':
    return render_template("hangman.html", the_title = "Juego del ahorcado")

@app.route("/compresorzip", methods = ["GET","POST"])
def compresor () -> 'html':
    if request.method == "POST":
        archivo = request.files['archivo']
        with open(archivo.filename, 'rb') as f_in:
            with gzip.open(archivo.filename+".gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return render_template("compresorzipresultado.html", the_title ='compresor zip',data=f_out)
    else:
        return render_template("compresorzip.html", the_title="Compresor de archivos a ZIP")

@app.route("/pdftoword", methods = ["GET","POST"])
def pdftotext () -> 'html':
    if request.method =="POST":
        archivo=request.files["archivo"]
        #pdf_file = 'Ejercicio+03.pdf'
        pdf_file = archivo.filename
        docx_file = pdf_file+'.docx'
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        return render_template('pdftoword.html', the_title='PDF to word', data = docx_file)
    else:
        return render_template("pdftoword.html", the_title="PDF to Word",data =None)

@app.route("/mailsender", methods = ["GET", "POST"])
def mailsender () -> 'html':
    if request.method=="POST":
        with open('textfile') as fp:
            msg = EmailMessage()
            msg.set_content()

        msg['Subject'] =f'The contents of {textfile}'
        msg['From'] = 'apostadormoi@gmail.com'
        msg['To'] = 'moissoto@gmail.com'

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
        return render_template ('mailsender.html', the_title = 'Enviar correo' )
    else:
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

app.run(debug=True)