from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

dataBase = sqlite3.connect('plantas.db', check_same_thread=False)
cursorDB = dataBase.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agregar')
def Agregar():
    return render_template('agregar.html')

@app.route('/galeria')
def Galeria():

    datos = cursorDB.execute('SELECT * FROM plantas')

    return render_template('galeria.html', registroDB=datos)
@app.route('/acercade')
def Acerca():
    return render_template('acercade.html')

@app.route('/agregar/datos', methods=['POST'])
def datos():
    
    nombre = request.form['nombrePlanta']
    nombre_cien = request.form['nombreCientifico']
    url = request.form['imagenURL']
    descripcion = request.form['descripcion']

    contenedor = (nombre, nombre_cien, url, descripcion)
    cursorDB.execute("INSERT INTO plantas(nombre, nombrecien, url, descripcion) VALUES (?, ?, ?, ?)", contenedor)
    dataBase.commit()

    alerta = 'Datos registrados correctamente'

    
    return render_template('agregar.html', alerta=alerta)

if __name__=='__main__':
    app.run(debug=True, port=456)
