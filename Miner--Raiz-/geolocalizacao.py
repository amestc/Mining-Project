import requests
from geopy.geocoders import Nominatim

def obter_endereco_por_cep(cep):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            dados = response.json()
            if "erro" not in dados:
                # Monta endereço completo
                endereco = f"{dados['logradouro']}, {dados['bairro']}, {dados['localidade']}, {dados['uf']}, Brasil"
                return endereco
    except Exception as e:
        print("Erro ao buscar endereço no ViaCEP:", e)
    return None

def obter_lat_lon(cep):
    cep_key = ''.join(filter(str.isdigit, str(cep)))
    geolocator = Nominatim(user_agent="mineradora-app")
    try:
        if cep_key and len(cep_key) == 8:
            location = geolocator.geocode({"postalcode": cep_key, "country": "Brazil"}, timeout=10)
        else:
            location = geolocator.geocode(cep, timeout=10)
        if location:
            return (location.latitude, location.longitude)
        else:
            print(f"CEP não encontrado: {cep_key}")
            return None, None
    except Exception as e:
        print(f"Erro ao buscar coordenadas para o CEP {cep_key}: {e}")
        return None, None

