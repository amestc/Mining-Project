from flask import Flask, jsonify, request
from flask_cors import CORS
from banco.dbmining import listar_maquinas, criar_maquina, atualizar_maquina, deletar_maquina
from py.functions_math import Distancia, AluguelTotal, CustoTotal, ValorTotal, CapacidadeTotal

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/maquinas', methods=['GET'])
def get_maquinas():
    maquinas = listar_maquinas()
    # Ordena pelo nome (você pode trocar para 'custo', 'kg', etc.)
    maquinas = sorted(maquinas, key=lambda m: m.nome)
    maquinas_dict = [
        {
            "custo": float(m.custo),
            "aluguel": float(m.aluguel),
            "kg": m.kg,
            "nome": m.nome,
            "id": m.id
        }
        for m in maquinas
    ]
    return jsonify(maquinas_dict)


@app.route('/maquinas', methods=['POST'])
def cadastrar_maquina():
    try:
        data = request.get_json()
        nome = data.get("nome")
        custo = data.get("custo")
        aluguel = data.get("aluguel")
        kg = data.get("kg")

        if not all([nome, custo, aluguel, kg]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400

        nova = criar_maquina(nome=nome, custo=custo, aluguel=aluguel, kg=kg)
        return jsonify({"mensagem": "Máquina cadastrada com sucesso!", "id": nova.id})
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/maquinas/<int:maquina_id>', methods=['PUT'])
def editar_maquina(maquina_id):
    try:
        data = request.get_json()
        nome = data.get("nome")
        custo = data.get("custo")
        aluguel = data.get("aluguel")
        kg = data.get("kg")

        if not all([nome, custo, aluguel, kg]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400

        maquina = atualizar_maquina(maquina_id, nome=nome, custo=custo, aluguel=aluguel, kg=kg)
        if maquina:
            return jsonify({"mensagem": "Máquina atualizada com sucesso!"})
        else:
            return jsonify({"erro": "Máquina não encontrada. 404"}), 404
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)} 500"}), 500

@app.route('/maquinas/<int:maquina_id>', methods=['DELETE'])
def excluir_maquina(maquina_id):
    try:
        sucesso = deletar_maquina(maquina_id)
        if sucesso:
            return jsonify({"mensagem": "Máquina excluída com sucesso!"})
        else:
            return jsonify({"erro": "Máquina não encontrada."}), 404
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)