from flask import Flask, request, jsonify

app = Flask(__name__)

# Banco de dados simples em memória
usuarios = []

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.json
    nome = dados.get('nome')
    email = dados.get('email')

    if not nome or not email:
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400

    usuario = {"nome": nome, "email": email}
    usuarios.append(usuario)

    return jsonify({"mensagem": "Usuário cadastrado", "usuario": usuario}), 201

@app.route('/usuarios', methods=['GET'])
def listar():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
