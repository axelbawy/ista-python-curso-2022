
from flask import Flask, jsonify, request

api = Flask(__name__)



if __name__=='__main__':
    api.run(debug= True, port=4000)