
from flask import Flask, jsonify, request
from email import message
from hashlib import new
import json


api = Flask(__name__)

def leer_archivo():
    archivo = None
    with open("./excel/estudiante.csv") as a:
        archivo = a.readlines()
    for row1 in archivo:
        partes= row1.split(',')
        data['lista'].append({
            "cedula": partes[0], "primer_apellido": partes[1], "segundo_apellido": partes[2], "primer_nombre": partes[3], "segundo_nombre": partes[4]
        })
    return data


@api.route('/obtenerEstudiante')
def procesar_informacion():
    contenido = leer_archivo()
    return jsonify(contenido)


@api.route('/obtenerEstudiante/<string:cedula>', methods=['PUT'])
def getestudiante(cedula):
    contenido = leer_archivo
    estudiante = [objeto for objeto in contenido['lista'] if objeto['cedula'] == cedula]
    return estudiante[0]

@api.route('/crearEstudiante', methods=['POST'])
def addEstudiante():
    new_Estudiante = {
        "cedula": request.json['cedula'], 
        "primer_apellido": request.json['primer_apellido'],  
        "segundo_apellido": request.json['segundo_apellido'],  
        "primer_nombre": request.json['primer_nombre'], 
        "segundo_nombre": request.json['segundo_nombre']
    }
    contenido = leer_archivo()
    contenido["lista"].append(new_Estudiante)
    return jsonify({
        "message" : "Agregado satisfactoriamente",
        "lista":contenido
    })

@api.route('/eliminarEstudiante/<string:cedula>', methods=['DELETE'])
def deleteEstudiante(cedula):
    contenido = leer_archivo
    estudiante = [objeto for objeto in contenido['lista'] if objeto['cedula'] == cedula]
    if len(estudiante)>0:
        contenido["lista"].remove(estudiante[0])
        return jsonify({
            "message" : "Agregado satisfactoriamente",
            "lista":contenido
        })
    return jsonify({
        "message" : "Estuduiante no encontrado",
    })

if __name__=='__main__':
    api.run(debug= True, port=4000)