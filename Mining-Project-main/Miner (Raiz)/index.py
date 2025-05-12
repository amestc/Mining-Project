from data.py import inserir, consultar, excluir, editar

class SistemaGerenciamento:
    def menu_principal(self):
        print("Como posso te chamar?")
        nome = input("Nome: ")
        print(f"\nSeja bem-vindo {nome}, selecione as opções abaixo:")

        while True:
            print("\n1. Máquinas\n2. Materiais\n3. Clientes\n4. Simular valor de operação\n0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao in ["1", "2", "3"]:
                entidade = ["Máquinas", "Materiais", "Clientes"][int(opcao)-1]
                self.menu_operacoes(entidade)
            elif opcao == "4":
                self.simular_operacao()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    def menu_operacoes(self, entidade):
        while True:
            print(f"\n--- {entidade.upper()} ---")
            print("1. Consultar\n2. Cadastrar\n3. Excluir\n4. Editar\n0. Voltar")
            opcao = input("Escolha: ")

            if opcao == "1":
                for item in consultar(entidade):
                    print(item)
            elif opcao == "2":
                self.cadastrar(entidade)
            elif opcao == "3":
                id_item = input("ID para excluir: ")
                excluir(entidade, id_item)
                print("Excluído com sucesso.")
            elif opcao == "4":
                self.editar(entidade)
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def cadastrar(self, entidade):
        if entidade == "Máquinas":
            dados = (
                input("Nome: "),
                input("Capacidade operacional: "),
                input("Custo aluguel por dia: "),
                input("Custo transporte: ")
            )
        elif entidade == "Materiais":
            dados = (
                input("Nome do material: "),
                input("Tipo: "),
                input("Dureza: ")
            )
        elif entidade == "Clientes":
            dados = (
                input("Nome do cliente: "),
                input("CPF: ")
            )
        inserir(entidade, dados)
        print(f"{entidade[:-1]} cadastrada com sucesso!")

    def editar(self, entidade):
        id_item = input("ID para editar: ")
        if entidade == "Máquinas":
            dados = (
                input("Novo nome: "),
                input("Nova capacidade: "),
                input("Novo custo aluguel/dia: "),
                input("Novo custo transporte: ")
            )
        elif entidade == "Materiais":
            dados = (
                input("Novo nome: "),
                input("Novo tipo: "),
                input("Nova dureza: ")
            )
        elif entidade == "Clientes":
            dados = (
                input("Novo nome: "),
                input("Novo CPF: ")
            )
        editar(entidade, id_item, dados)
        print("Editado com sucesso!")

    def simular_operacao(self):
        print("\nSimulação de operação:")
        id_maquina = input("ID da máquina: ")
        id_material = input("ID do material: ")
        qtd_material = input("Qtd. de materiais: ")
        id_cliente = input("ID do cliente: ")
        local = input("Local: ")

        # Apenas simulação estática por enquanto
        print("\nResultado:")
        print(f"Máquina: {id_maquina}, Material: {id_material}, Quantidade: {qtd_material}, Cliente: {id_cliente}, Local: {local}, Valor: R$1000,00")

        while True:
            print("\n1. Voltar ao menu\n2. Nova simulação")
            opcao = input("Escolha: ")
            if opcao == "1":
                break
            elif opcao == "2":
                self.simular_operacao()
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    sistema = SistemaGerenciamento()
    sistema.menu_principal()
