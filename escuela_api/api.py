from distutils.log import debug
from email import message_from_binary_file
from hashlib import new
import json
from flask import api, jsonify, request
from flask.api import jsonify, request

app = api(__name__)

def leer_archivo():
    archivo = None
    with open("estudiante.csv") as a:
        archivo = a.readline()
    return archivo

@app.route('/obtenerDatosEstudiante')
def mostrarDatos():
    contenido = leer_archivo()
    partes = [contenido1 for contenido1 in contenido]
    for x in partes:
        part = x.split(',')
        new_estudiante= {
            "cedula": partes [0],"primer_apellido": partes [1],"segundo_apellido": partes [2],"primer_nombre":partes [3],"segundo_nombre":partes [4]
        }
    return jsonify(new_estudiante)

if __name__=='__main__':
    app.run(debug=true, port=4000)