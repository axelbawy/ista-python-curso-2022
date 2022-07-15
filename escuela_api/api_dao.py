from flask import Flask, jsonify

app = Flask(__name__)

def leer_archivo():
    archivo = None
    with open("estudiante.csv") as a:
        archivo = a.readlines()
    return archivo

@app.route('/obtener_datos')
def procesar_informacion():
    contenido = leer_archivo()
    #Procesamiento de la línea del archivo!
    partes = contenido[0].split(',')
    return jsonify({"cedula": partes[0], "primer_apellido": partes[1], "segundo_apellido": partes[2], "primer_nombre": partes[3], "segundo_nombre": partes[4]})