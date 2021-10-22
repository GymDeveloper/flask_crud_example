from flask import Flask, render_template, request, redirect
from controller import insert_employee

# debo decirle a mi app que pueda cargar la carpeta tempates
app = Flask(__name__, template_folder="templates")


# Esta la ruta raiz
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/crear')
def create():
    return render_template('create.html')


# debo crear una ruta de tipo POST que se encargue de recibir
# la información de mi html y guardarlo en la base de datos
@app.route('/store-employee', methods=['POST'])
def store():
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    position = request.form['position']
    # esta funcion guardar la informacion en la base de datos
    insert_employee(name, last_name, email, position)
    return redirect('/')


# Vamos inicializar nuestro servidor con flask
app.run(host='localhost', port=5000)
