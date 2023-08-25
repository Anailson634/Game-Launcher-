from flask import Flask, request, jsonify
from flask_cors import CORS
from manipulador_json import json_back as JSB
from os import system as sys 

app = Flask(__name__)
CORS(app)
arq_json=JSB()

@app.route('/', methods=['GET'])
def get_dados():
    # Aqui é onde carregamos os dados do arquivo json
    return arq_json.carregar()

@app.route('/iniciar', methods=['POST'])
def response_front():
    response_date=request.json

    local_exe=response_date["Game"].replace("//", "/")
    sys(f"start {local_exe}")
    

    response={'Sucesso': 'Update realizado com sucesso'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
