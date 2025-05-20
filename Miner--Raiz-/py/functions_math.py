from banco.dbmining import session, Maquinas, Materiais, Clientes

# Funções para calcular valores relacionados a máquinas e materiais
def get_maquina_por_id(maquina_id):
    return session.query(Maquinas).filter_by(id=maquina_id).first()

def get_material_por_id(material_id):
    return session.query(Materiais).filter_by(id=material_id).first()

# Função para determinar distancia inicial e final

# Em resumo, aqui a gente vai colocar que a distancia inicial vai ser de nós,
# podemos colocar que a gente é a fecaf, e final vai ser o cliente
# e depois vamos ter que inverter os valores para definir o calculo da volta da maquina

def DistanciaCliente(cliente_id):
    cliente = session.query(Clientes).filter_by(id=cliente_id).first()
    if cliente:
        return cliente.cep
    return None

# Função para calcular a distância entre dois pontos
def Distancia(distancia_cliente, distancia_equipe):
    distancia1 = distancia_cliente
    distancia2 = distancia_equipe
    return (distancia1 - distancia2) + (distancia2 - distancia1)

# Funções para calcular valores totais
def AluguelTotal(maquina_id, dias):
    maquina = get_maquina_por_id(maquina_id)
    if maquina:
        return float(maquina.aluguel) * dias
    return None

def CustoTotal(maquina_id):
    maquina = get_maquina_por_id(maquina_id)
    if maquina:
        return float(maquina.custo) * Distancia
    return None

def ValorTotal(maquina_id, dias):
    aluguel_total = AluguelTotal(maquina_id, dias)
    custo_total = CustoTotal(maquina_id, Distancia)
    if aluguel_total is not None and custo_total is not None:
        return aluguel_total + custo_total
    return None

def CapacidadeTotal(maquina_id, material_id):
    maquina = get_maquina_por_id(maquina_id)
    material = get_material_por_id(material_id)
    if maquina and material and material.dureza != 0:
        return float(maquina.kg) / float(material.dureza)
    return None