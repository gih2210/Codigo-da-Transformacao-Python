from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/somar', methods=['POST'])
def somar():
    dados = request.get_json()
    if not dados or 'a' not in dados or 'b' not in dados:
        return jsonify({"erro": "Entrada inválida"}), 400
    
    resultado = dados['a'] + dados['b']
    return jsonify({"resultado": resultado}), 200

if __name__ == '__main__':
    app.run(debug=True)