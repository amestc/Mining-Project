class SistemaGerenciamento:
    def __init__(self):
        self.maquinas = []
        self.materiais = []
        self.clientes = []
        self.simulacoes = []
        
    def menu_principal(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Máquinas")
            print("2. Materiais")
            print("3. Clientes")
            print("4. Simular valor de operação")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.menu_operacoes("Máquinas")
            elif opcao == "2":
                self.menu_operacoes("Materiais")
            elif opcao == "3":
                self.menu_operacoes("Clientes")
            elif opcao == "4":
                self.simular_operacao()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def menu_operacoes(self, entidade):
        while True:
            print(f"\n=== MENU {entidade.upper()} ===")
            print(f"1. Consultar {entidade}")
            print(f"2. Cadastrar {entidade}")
            print(f"3. Excluir {entidade}")
            print(f"4. Editar {entidade}")
            print("0. Voltar ao menu principal")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.consultar(entidade)
            elif opcao == "2":
                self.cadastrar(entidade)
            elif opcao == "3":
                self.excluir(entidade)
            elif opcao == "4":
                self.editar(entidade)
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def cadastrar(self, entidade):
        print(f"\n=== CADASTRAR {entidade.upper()} ===")
        
        if entidade == "Máquinas":
            dados = {
                "nome_maquina": input("Nome da máquina: "),
                "capacidade_operacional": input("Capacidade operacional (ex: tomos,alagens): "),
                "curso_transporte": input("Curso de transporte (ex: por km ou m): ")
            }
            self.maquinas.append({"id": len(self.maquinas)+1, **dados})
            
        elif entidade == "Materiais":
            dados = {
                "nome_material": input("Nome do material: "),
                "tipo": input("Tipo: "),
                "dureza": input("Dureza: ")
            }
            self.materiais.append({"id": len(self.materiais)+1, **dados})
            
        elif entidade == "Clientes":
            dados = {
                "nome_cliente": input("Nome do cliente: "),
                "cpf": input("CPF: ")
            }
            self.clientes.append({"id": len(self.clientes)+1, **dados})
        
        print(f"{entidade[:-1]} cadastrad{ 'a' if entidade[-1] == 's' else 'o'} com sucesso!")
    
    def consultar(self, entidade):
        print(f"\n=== CONSULTAR {entidade.upper()} ===")
        
        lista = getattr(self, entidade.lower())
        
        if not lista:
            print(f"Nenhum{ 'a' if entidade[-1] == 's' else 'o'} {entidade.lower()} cadastrad{ 'a' if entidade[-1] == 's' else 'o'}.")
            return
        
        for item in lista:
            print("\n" + "-"*30)
            for chave, valor in item.items():
                print(f"{chave.replace('_', ' ').title()}: {valor}")
    
    def excluir(self, entidade):
        self.consultar(entidade)
        lista = getattr(self, entidade.lower())
        
        if not lista:
            return
            
        id_excluir = input(f"\nDigite o ID d{ 'a' if entidade[-1] == 's' else 'o'} {entidade.lower()} a ser excluíd{ 'a' if entidade[-1] == 's' else 'o'}: ")
        
        try:
            id_excluir = int(id_excluir)
            lista[:] = [item for item in lista if item["id"] != id_excluir]
            print(f"{entidade[:-1]} excluíd{ 'a' if entidade[-1] == 's' else 'o'} com sucesso!")
        except ValueError:
            print("ID inválido.")
    
    def editar(self, entidade):
        self.consultar(entidade)
        lista = getattr(self, entidade.lower())
        
        if not lista:
            return
            
        id_editar = input(f"\nDigite o ID d{ 'a' if entidade[-1] == 's' else 'o'} {entidade.lower()} a ser editad{ 'a' if entidade[-1] == 's' else 'o'}: ")
        
        try:
            id_editar = int(id_editar)
            item = next((x for x in lista if x["id"] == id_editar), None)
            
            if item:
                print("\nDeixe em branco para manter o valor atual.")
                for chave in item.keys():
                    if chave != "id":
                        novo_valor = input(f"{chave.replace('_', ' ').title()} (atual: {item[chave]}): ")
                        if novo_valor:
                            item[chave] = novo_valor
                print(f"{entidade[:-1]} atualizad{ 'a' if entidade[-1] == 's' else 'o'} com sucesso!")
            else:
                print("ID não encontrado.")
        except ValueError:
            print("ID inválido.")
    
    def simular_operacao(self):
        print("\n=== SIMULAR VALOR DE OPERAÇÃO ===")
        
        print("\nSelecione os IDs necessários:")
        self.consultar("Máquinas")
        id_maquina = input("\nID da máquina: ")
        
        self.consultar("Materiais")
        id_material = input("ID do material: ")
        
        self.consultar("Clientes")
        id_cliente = input("ID do cliente: ")
        
        onda_materiais = input("Onda de materiais: ")
        local = input("Local: ")
        
        # Aqui viria a lógica de cálculo do valor da operação
        # Por simplicidade, vamos apenas armazenar os dados
        simulacao = {
            "id_maquina": id_maquina,
            "id_material": id_material,
            "id_cliente": id_cliente,
            "onda_materiais": onda_materiais,
            "local": local,
            "valor": "1000.00"  # Valor simulado
        }
        self.simulacoes.append(simulacao)
        
        print("\n=== RESULTADO DA SIMULAÇÃO ===")
        for chave, valor in simulacao.items():
            print(f"{chave.replace('_', ' ').title()}: {valor}")
        
        while True:
            print("\n1. Voltar ao menu")
            print("2. Nova simulação")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                break
            elif opcao == "2":
                self.simular_operacao()
                break
            else:
                print("Opção inválida.")

# Iniciar o sistema
if __name__ == "__main__":
    sistema = SistemaGerenciamento()
    sistema.menu_principal()