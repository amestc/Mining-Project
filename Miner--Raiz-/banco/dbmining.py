from sqlalchemy import create_engine#Estou startando a conexão com o banco de dados
from sqlalchemy import Column, Integer, String, Numeric, PrimaryKeyConstraint #Estou importando os tipos de dados que vou usar nas colunas das tabelas
from sqlalchemy.orm import sessionmaker #Estou importando o sessionmaker para criar uma sessão com o banco de dados
from sqlalchemy.ext.declarative import declarative_base #Estou importando o declarative_base para criar as classes que representam as tabelas do banco de dados
db = create_engine("mysql+pymysql://root:root123@127.0.0.1:3306/mineradora")#Aqui eu passo os parametros de conexão com o banco de dados, como Usuario:senha:ip do banco:nome

Session = sessionmaker(bind=db) #Aqui eu crio uma sessão com o banco de dados
session = Session() #Aqui eu crio uma sessão com o banco de dados

base = declarative_base() #Aqui eu crio uma base declarativa para criar as classes que representam as tabelas do banco de dados

class Maquinas(base):
    __tablename__ = "maquinas" #Aqui eu defino o nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True) #Aqui eu defino a coluna id como chave primária
    nome = Column(String(50)) #Aqui eu defino a coluna nome como string com tamanho 50
    custo = Column(Numeric(10,2)) #Aqui eu defino a coluna tipo como float com tamanho 10 e 2 casas decimais
    aluguel = Column(Numeric(10,2)) #Aqui eu defino a coluna aluguel como float com tamanho 10 e 2 casas decimais
    kg = Column(Integer) #Aqui eu defino a coluna ano como inteiro
    
    def __init__(self, nome, custo, kg, aluguel): #Aqui eu crio o construtor da classe
        self.nome = nome #Aqui eu defino o nome da maquina
        self.custo = custo #Aqui eu defino o custo da maquina
        self.kg = kg #Aqui eu defino o peso da maquina
        self.aluguel = aluguel
class Materiais(base):
    __tablename__ = "materiais" #Aqui eu defino o nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True) #Aqui eu defino a coluna id como chave primária
    nome = Column(String(50)) #Aqui eu defino a coluna nome como string com tamanho 50
    tipo = Column(String (50)) #Aqui eu defino a coluna tipo como string com tamanho 50
    peso = Column(Integer) #Aqui eu defino a coluna peso como inteiro

    def __init__(self, nome, tipo, peso): #Aqui eu crio o construtor da classe   
        self.nome = nome #Aqui eu defino o nome do material
        self.tipo = tipo #Aqui eu defino o tipo do material
        self.peso = peso #Aqui eu defino a peso do material
class Clientes(base):
    __tablename__ = "clientes" #Aqui eu defino o nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True) #Aqui eu defino a coluna id como chave primária
    nome = Column(String(50)) #Aqui eu defino a coluna nome como string com tamanho 50
    cpf_cnpj = Column(String(20)) #Aqui eu defino a coluna cpf/cnpj como string com tamanho 20
    nome_fantasia = Column(String(50)) #Aqui eu defino a coluna telefone como string com tamanho 50
    cep = Column(String(9)) #Aqui eu defino a coluna localização como string com tamanho 50

    def __init__(self, nome, cpf_cnpj, nome_fantasia, cep): #Aqui eu crio o construtor da classe
        self.nome = nome #Aqui eu defino o nome do cliente
        self.cpf_cnpj = cpf_cnpj #Aqui eu defino o cpf/cnpj do cliente
        self.nome_fantasia = nome_fantasia #Aqui eu defino o nome fantasia do cliente
        self.cep = cep #Aqui eu defino a localização do cliente

base.metadata.create_all(db) #Aqui eu crio as tabelas no banco de dados

#-------------------------------------------------------------------------------------------------------------------------------------

# Funções CRUD para Maquinas
def criar_maquina(nome, custo, aluguel, kg):
    maquina = Maquinas(nome=nome, custo=custo, aluguel=aluguel, kg=kg)
    session.add(maquina)
    session.commit()
    return maquina

def listar_maquinas():
    session = Session()
    try:
        return session.query(Maquinas).all()
    except Exception as e:
        session.rollback()
        print("Erro ao listar máquinas:", e)
        return []
    finally:
        session.close()

def atualizar_maquina(id, nome=None, custo=None, aluguel=None, kg=None):
    maquina = session.query(Maquinas).filter_by(id=id).first()
    if not maquina:
        return None
    if nome is not None:
        maquina.nome = nome
    if custo is not None:
        maquina.custo = custo
    if aluguel is not None:
        maquina.aluguel = aluguel
    if kg is not None:
        maquina.kg = kg
    session.commit()
    return maquina

def deletar_maquina(id):
    maquina = session.query(Maquinas).filter_by(id=id).first()
    if not maquina:
        return False
    session.delete(maquina)
    session.commit()
    return True

# Funções CRUD para Materiais
def criar_material(nome, tipo, peso):
    material = Materiais(nome=nome, tipo=tipo, peso=peso)
    session.add(material)
    session.commit()
    return material

def listar_materiais():
    session = Session()
    try:
        return session.query(Materiais).all()
    except Exception as e:
        session.rollback()
        print("Erro ao listar materiais:", e)
        return []
    finally:
        session.close()

def atualizar_material(id, nome=None, tipo=None, peso=None):
    material = session.query(Materiais).filter_by(id=id).first()
    if not material:
        return None
    if nome is not None:
        material.nome = nome
    if tipo is not None:
        material.tipo = tipo
    if peso is not None:
        material.peso = peso
    session.commit()
    return material

def deletar_material(id):
    material = session.query(Materiais).filter_by(id=id).first()
    if not material:
        return False
    session.delete(material)
    session.commit()
    return True

# Funções CRUD para Clientes
def criar_cliente(nome, nome_fantasia, cpf_cnpj, cep):
    cliente = Clientes(nome=nome, nome_fantasia=nome_fantasia, cpf_cnpj=cpf_cnpj, cep=cep)
    session.add(cliente)
    session.commit()
    return cliente

def listar_clientes():
    return session.query(Clientes).all()

def atualizar_cliente(id, nome=None, nome_fantasia=None, cpf_cnpj=None, cep=None):
    cliente = session.query(Clientes).filter_by(id=id).first()
    if not cliente:
        return None
    if nome is not None:
        cliente.nome = nome
    if nome_fantasia is not None:
        cliente.nome_fantasia = nome_fantasia
    if cpf_cnpj is not None:
        cliente.cpf_cnpj = cpf_cnpj
    if cep is not None:
        cliente.cep = cep
    session.commit()
    return cliente

def deletar_cliente(id):
    cliente = session.query(Clientes).filter_by(id=id).first()
    if not cliente:
        return False
    session.delete(cliente)
    session.commit()
    return True

def get_cliente_por_id(cliente_id):
    from .dbmining import session, Clientes
    return session.query(Clientes).filter_by(id=cliente_id).first()
