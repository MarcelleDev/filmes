from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Caminho do arquivo JSON
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'filmes.json')

# Carregar filmes do arquivo JSON
def carregar_filmes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Salvar filmes no arquivo JSON
def salvar_filmes(filmes):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(filmes, f, ensure_ascii=False, indent=4)

# Rotas
@app.route('/')
def index():
    return render_template('index.html')

# API para CRUD
@app.route('/filmes', methods=['GET', 'POST'])
def filmes():
    if request.method == 'GET':
        filmes = carregar_filmes()
        return jsonify(filmes)
    elif request.method == 'POST':
        novo_filme = request.json
        filmes = carregar_filmes()
        filmes.append(novo_filme)
        salvar_filmes(filmes)
        return jsonify({"message": "Filme adicionado!"}), 201

@app.route('/filmes/<int:id>', methods=['PUT', 'DELETE'])
def filme(id):
    filmes = carregar_filmes()
    if id < 0 or id >= len(filmes):
        return jsonify({"error": "Filme não encontrado"}), 404

    if request.method == 'PUT':
        filme_atualizado = request.json
        filmes[id] = filme_atualizado
        salvar_filmes(filmes)
        return jsonify({"message": "Filme atualizado!"})
    elif request.method == 'DELETE':
        del filmes[id]
        salvar_filmes(filmes)
        return jsonify({"message": "Filme removido!"})

if __name__ == '__main__':
    app.run(debug=True) 