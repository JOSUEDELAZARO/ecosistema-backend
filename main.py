from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Ecosistema Multi-IA Backend en funcionamiento."

@app.route('/procesar', methods=['POST'])
def procesar():
    datos = request.json
    return jsonify({'respuesta': f"Procesado: {datos}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
