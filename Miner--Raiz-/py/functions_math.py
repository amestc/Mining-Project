from banco.dbmining import session, Maquinas, Materiais, Clientes
from geolocalizacao import obter_lat_lon
import math
import requests

def get_maquina_por_id(maquina_id):
    return session.query(Maquinas).filter_by(id=maquina_id).first()

def get_material_por_id(material_id):
    return session.query(Materiais).filter_by(id=material_id).first()

def get_cliente_por_id(cliente_id):
    return session.query(Clientes).filter_by(id=cliente_id).first()

def LatLonCliente(cliente_id):
    cliente = session.query(Clientes).filter_by(id=cliente_id).first()
    if not cliente or not cliente.cep:
        return None, None
    cep = ''.join(filter(str.isdigit, str(cliente.cep)))
    from geolocalizacao import obter_lat_lon
    lat, lon = obter_lat_lon(cep)
    return lat, lon


def Distancia_por_cep(cep):
    # Coordenadas fixas da base
    lat1 = -23.610853
    lon1 = -46.7679255

    lat2, lon2 = obter_lat_lon(cep)
    if lat2 is None or lon2 is None:
        print(f"Não foi possível obter coordenadas para o CEP {cep}")
        return None
    R = 6371  # Raio da Terra em km
    X1 = math.radians(lat1)
    X2 = math.radians(lat2)
    Y1 = math.radians(lon1)
    Y2 = math.radians(lon2)

    # Diferenças
    delta_X = X2 - X1
    delta_Y = Y2 - Y1

    # Cálculo
    a = math.sin(delta_X / 2)**2 + math.cos(X1) * math.cos(X2) * math.sin(delta_Y / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    d = R * c

    print(d)
    return d # Distância em km

def AluguelTotal(maquina_id, dias):
    maquina = get_maquina_por_id(maquina_id)
    if maquina:
        return float(maquina.aluguel) * dias
    return None

def CustoTotal(maquina_id, cep):
    maquina = get_maquina_por_id(maquina_id)
    distancia = Distancia_por_cep(cep)
    if maquina and distancia is not None:
        return (distancia * 6.36) + float(maquina.custo)
    return None

def ValorTotal(maquina_id, cep, dias):
    aluguel_total = AluguelTotal(maquina_id, dias)
    custo_total = CustoTotal(maquina_id, cep)
    if aluguel_total is not None and custo_total is not None:
        return aluguel_total + custo_total
    return None

def CapacidadeTotal(maquina_id, material_id):
    maquina = get_maquina_por_id(maquina_id)
    material = get_material_por_id(material_id)
    if maquina and material and material.peso != 0:
        return float(maquina.kg) / float(material.peso)
    return None

def obter_lat_lon(cep_ou_endereco):
    from geopy.geocoders import Nominatim
    import requests

    # Remove espaços extras
    entrada = cep_ou_endereco.strip()
    # Se for só números e tiver 8 dígitos, trata como CEP
    if entrada.isdigit() and len(entrada) == 8:
        geolocator = Nominatim(user_agent="mineradora-app")
        try:
            location = geolocator.geocode({"postalcode": entrada, "country": "Brazil"}, timeout=10)
            if not location:
                # Tenta buscar endereço pelo ViaCEP
                resp = requests.get(f"https://viacep.com.br/ws/{entrada}/json/")
                if resp.ok:
                    data = resp.json()
                    if "erro" not in data:
                        endereco = f"{data['logradouro']}, {data['bairro']}, {data['localidade']}, {data['uf']}, Brasil"
                        location = geolocator.geocode(endereco, timeout=10)
            if location:
                return (location.latitude, location.longitude)
            else:
                print(f"CEP não encontrado: {entrada}")
                return None, None
        except Exception as e:
            print(f"Erro ao buscar coordenadas para o CEP {entrada}: {e}")
            return None, None
    else:
        # Trata como endereço completo
        geolocator = Nominatim(user_agent="mineradora-app")
        try:
            location = geolocator.geocode(entrada, timeout=10)
            if location:
                return (location.latitude, location.longitude)
            else:
                print(f"Endereço não encontrado: {entrada}")
                return None, None
        except Exception as e:
            print(f"Erro ao buscar coordenadas para o endereço {entrada}: {e}")
            return None, None
    