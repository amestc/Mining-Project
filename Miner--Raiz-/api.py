from flask import Flask, jsonify, request
from flask_cors import CORS
from banco.dbmining import (
    listar_maquinas, criar_maquina, atualizar_maquina, deletar_maquina,
    listar_clientes, criar_cliente, atualizar_cliente, deletar_cliente,
    listar_materiais, criar_material, atualizar_material, deletar_material,
    get_cliente_por_id  # <-- Adicione esta linha
)
from py.functions_math import AluguelTotal, CustoTotal, ValorTotal, CapacidadeTotal, Distancia_por_cep

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
def listar_clientes():
    try:
        from banco.dbmining import listar_clientes
        clientes = listar_clientes()
        return jsonify([
            {
                "id": c.id,
                "nome": c.nome,
                "nome_fantasia": c.nome_fantasia,
                "cpf_cnpj": c.cpf_cnpj,
                "cep": c.cep
            } for c in clientes
        ])
    except Exception as e:
        print("Erro ao listar clientes:", e)
        return jsonify([]), 500

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
def listar_materiais():
    try:
        from banco.dbmining import listar_materiais
        materiais = listar_materiais()
        return jsonify([
            {
                "id": m.id,
                "nome": m.nome,
                "tipo": m.tipo,
                "peso": m.peso
            } for m in materiais
        ])
    except Exception as e:
        print("Erro ao listar materiais:", e)
        return jsonify([]), 500

@app.route('/materiais', methods=['POST'])
def cadastrar_material():
    try:
        data = request.get_json()
        nome = data.get("nome")
        tipo = data.get("tipo")
        peso = data.get("peso")
        if not all([nome, tipo, peso]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400
        novo = criar_material(nome=nome, tipo=tipo, peso=peso)
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
        peso = data.get("peso")
        if not all([nome, tipo, peso]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400
        material = atualizar_material(material_id, nome=nome, tipo=tipo, peso=peso)
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

# --- SIMULAÇÃO ---
@app.route('/simulacao/calcular', methods=['POST'])
def simular():
    try:
        data = request.get_json()
        maquina_id = data.get('maquina_id')
        material_id = data.get('material_id')
        cep = data.get('cep')
        dias = data.get('dias')

        if not all([maquina_id, material_id, cep, dias]):
            return jsonify({"erro": "Todos os campos são obrigatórios."}), 400

        distancia = Distancia_por_cep(cep)
        if distancia is None:
            return jsonify({"erro": "Não foi possível calcular a distância. Verifique se o CEP está correto."}), 400

        aluguel_total = AluguelTotal(maquina_id, dias)
        custo_total = CustoTotal(maquina_id, cep)
        valor_total = ValorTotal(maquina_id, cep, dias)
        capacidade_total = CapacidadeTotal(maquina_id, material_id)

        return jsonify({
            "distancia": distancia,
            "aluguel_total": aluguel_total,
            "custo_total": custo_total,
            "valor_total": valor_total,
            "capacidade_total": capacidade_total
        })
    except Exception as e:
        print("Erro interno:", str(e))
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500




if __name__ == '__main__':
    app.run(debug=True)