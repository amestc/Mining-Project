from flask import Flask, jsonify
from flask_cors import CORS
from banco.dbmining import listar_maquinas

app = Flask(__name__)
CORS(app)

@app.route('/maquinas')
def get_maquinas():
    maquinas = listar_maquinas()
    # Ordena pelo nome (você pode trocar para 'custo', 'kg', etc.)
    maquinas = sorted(maquinas, key=lambda m: m.nome)
    maquinas_dict = [
        {
            "custo": float(m.custo),
            "aluguel": float(m.aluguel),
            "kg": m.kg,
            "nome": m.nome
        }
        for m in maquinas
    ]
    return jsonify(maquinas_dict)

if __name__ == '__main__':
    app.run(debug=True)