import requests
from geopy.geocoders import Nominatim
import time

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

def obter_lat_lon(endereco):
    geolocator = Nominatim(user_agent="cep_geocoder")
    try:
        location = geolocator.geocode(endereco)
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print("Erro ao buscar coordenadas:", e)
    return None, None

# Entrada do usuário
cep = input("Digite o CEP (apenas números): ").replace("-", "").strip()

endereco = obter_endereco_por_cep(cep)
if endereco:
    print("Endereço encontrado:", endereco)
    latitude, longitude = obter_lat_lon(endereco)
    if latitude and longitude:
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Não foi possível obter coordenadas para o endereço.")
else:
    print("CEP inválido ou não encontrado.")
