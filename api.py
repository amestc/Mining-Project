from flask import Flask, jsonify, request
from flask_cors import CORS
from banco.dbmining import (
    listar_maquinas, criar_maquina, atualizar_maquina, deletar_maquina,
    listar_clientes, criar_cliente, atualizar_cliente, deletar_cliente,
    listar_materiais, criar_material, atualizar_material, deletar_material
)
from py.functions_math import Distancia, AluguelTotal, CustoTotal, ValorTotal, CapacidadeTotal

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

# --- MÁQUINAS ---
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

# --- CLIENTES ---
@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = listar_clientes()
    clientes_dict = [
        {
            "id": c.id,
            "nome": c.nome,
            "nome_fantasia": c.nome_fantasia,
            "cpf_cnpj": c.cpf_cnpj,
            "cep": c.cep
        }
        for c in clientes
    ]
    return jsonify(clientes_dict)

@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():
    try:
        data = request.get_json()
        nome = data.get("nome")
        nome_fantasia = data.get("nome_fantasia")
        cpf_cnpj = data.get("cpf_cnpj")
        cep = data.get("cep")
        if not all([nome, nome_fantasia, cpf_cnpj, cep]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400
        novo = criar_cliente(nome=nome, nome_fantasia=nome_fantasia, cpf_cnpj=cpf_cnpj, cep=cep)
        return jsonify({"mensagem": "Cliente cadastrado com sucesso!", "id": novo.id})
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def editar_cliente(cliente_id):
    try:
        data = request.get_json()
        nome = data.get("nome")
        nome_fantasia = data.get("nome_fantasia")
        cpf_cnpj = data.get("cpf_cnpj")
        cep = data.get("cep")
        if not all([nome, nome_fantasia, cpf_cnpj, cep]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400
        cliente = atualizar_cliente(cliente_id, nome=nome, nome_fantasia=nome_fantasia, cpf_cnpj=cpf_cnpj, cep=cep)
        if cliente:
            return jsonify({"mensagem": "Cliente atualizado com sucesso!"})
        else:
            return jsonify({"erro": "Cliente não encontrado."}), 404
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def excluir_cliente(cliente_id):
    try:
        sucesso = deletar_cliente(cliente_id)
        if sucesso:
            return jsonify({"mensagem": "Cliente excluído com sucesso!"})
        else:
            return jsonify({"erro": "Cliente não encontrado."}), 404
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

# --- MATERIAIS ---
@app.route('/materiais', methods=['GET'])
def get_materiais():
    materiais = listar_materiais()
    materiais_dict = [
        {
            "id": m.id,
            "nome": m.nome,
            "tipo": m.tipo,
            "dureza": m.dureza
        }
        for m in materiais
    ]
    return jsonify(materiais_dict)

@app.route('/materiais', methods=['POST'])
def cadastrar_material():
    try:
        data = request.get_json()
        nome = data.get("nome")
        tipo = data.get("tipo")
        dureza = data.get("dureza")
        if not all([nome, tipo, dureza]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400
        novo = criar_material(nome=nome, tipo=tipo, dureza=dureza)
        return jsonify({"mensagem": "Material cadastrado com sucesso!", "id": novo.id})
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/materiais/<int:material_id>', methods=['PUT'])
def editar_material(material_id):
    try:
        data = request.get_json()
        nome = data.get("nome")
        tipo = data.get("tipo")
        dureza = data.get("dureza")
        if not all([nome, tipo, dureza]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400
        material = atualizar_material(material_id, nome=nome, tipo=tipo, dureza=dureza)
        if material:
            return jsonify({"mensagem": "Material atualizado com sucesso!"})
        else:
            return jsonify({"erro": "Material não encontrado."}), 404
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/materiais/<int:material_id>', methods=['DELETE'])
def excluir_material(material_id):
    try:
        sucesso = deletar_material(material_id)
        if sucesso:
            return jsonify({"mensagem": "Material excluído com sucesso!"})
        else:
            return jsonify({"erro": "Material não encontrado."}), 404
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)