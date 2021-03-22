import pymongo as mongo
from flask import Flask, render_template, request

Conn = mongo.MongoClient("mongodb://localhost:27017/")
db = Conn["IoT_Arduino"]
coll = db["Medicion"]

app = Flask(__name__)

t = 0
h = 0

@app.route('/')
def index():
    return 'Página inicial, consulta de temperatura y humedad'

@app.route('/cargar/')
def cargar():
    return render_template('PaginaPrueba.html',temperatura = t, humedad = h)

@app.route('/guardar/')
def guardar():

    global t
    global h
    t = request.args.get('temperatura')
    h = request.args.get('humedad')
    archivo = {"Temperatura": t, "Humedad": h }
    coll.insert(archivo)
    return render_template('PaginaPrueba.html',temperatura = t, humedad = h)

   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')