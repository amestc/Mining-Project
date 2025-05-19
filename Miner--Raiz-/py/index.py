from banco.dbmining import criar_maquina, criar_material, criar_cliente, listar_materiais, listar_clientes, listar_maquinas, atualizar_cliente, atualizar_maquina, atualizar_material, deletar_cliente, deletar_maquina, deletar_material

class SistemaGerenciamento:
    def menu_principal(self):
        print("Como posso te chamar?")
        nome = input("Nome: ")
        print(f"\nSeja bem-vindo {nome}, selecione as opções abaixo:")

        while True:
            print("\n1. Máquinas\n2. Materiais\n3. Clientes\n4. Simular valor de operação\n0. Sair")
            opcao = input("Escolha uma opção: ")

            match opcao:
                case "1":
                    while True:
                        print("\n. MÁQUINAS\n\n1. Cadastrar\n2. Pesquisar\n3. Editar\n4. Excluir\n0. Voltar")
                        escolha = input("Escolha uma opção: ")
                        if escolha == "0":
                            break  # Volta para o menu principal
                        elif escolha == "1":
                            nome = input("Nome da máquina: ")
                            custo = float(input("Aluguel da máquina: "))
                            kg = int(input("Peso (kg) da máquina: "))
                            criar_maquina(nome, custo, kg)
                            print("\nMáquinas cadastradas:")
                            for m in listar_maquinas():
                                print(m.id, m.nome, m.custo, m.kg)
                        elif escolha == "2":
                            termo = input("Digite o nome (ou parte) da máquina para pesquisar: ").lower()
                            encontrados = [m for m in listar_maquinas() if termo in m.nome.lower()]
                            if encontrados:
                                print("\nResultados encontrados:")
                                for m in encontrados:
                                    print(m.id, m.nome, m.custo, m.kg)
                            else:
                                print("Nenhuma máquina encontrada com esse nome.")
                        elif escolha == "3":
                            id_editar = input("Digite o ID da máquina que deseja editar: ")
                            maquinas = listar_maquinas()
                            maquina = next((m for m in maquinas if str(m.id) == id_editar), None)
                            if maquina:
                                novo_nome = input(f"Novo nome [{maquina.nome}]: ") or maquina.nome
                                novo_custo = input(f"Novo aluguel [{maquina.custo}]: ") or maquina.custo
                                novo_kg = input(f"Novo peso (kg) [{maquina.kg}]: ") or maquina.kg
                                # Atualize usando a função de update (você precisa ter uma função atualizar_maquina)
                                atualizar_maquina(maquina.id, novo_nome, float(novo_custo), int(novo_kg))
                                print("Máquina atualizada com sucesso!")
                            else:
                                print("Máquina não encontrada.")
                        elif escolha == "4":
                            id_excluir = input("Digite o ID da máquina que deseja excluir: ")
                            maquinas = listar_maquinas()
                            maquina = next((m for m in maquinas if str(m.id) == id_excluir), None)
                            if maquina:
                                deletar_maquina(maquina.id)
                                print("Máquina excluída com sucesso!")
                            else:
                                print("Máquina não encontrada.")
                case "2":
                    while True:
                        print("\n. MATERIAL\n\n1. Cadastrar\n2. Pesquisar\n3. Editar\n4. Excluir\n0. Voltar")
                        escolha = input("Escolha uma opção: ")
                        if escolha == "0":
                            break
                        elif escolha == "1":
                            nome = input("Nome do material: ")
                            tipo = input("Tipo de material: ")
                            dureza = int(input("Dureza do material: "))
                            criar_material(nome, tipo, dureza)
                            print("\nMateriais cadastrados:")
                            for n in listar_materiais():
                                print(n.id, n.nome, n.tipo, n.dureza)
                        elif escolha == "2":
                            termo = input("Digite o nome (ou parte) do material para pesquisar: ").lower()
                            encontrados = [n for n in listar_materiais() if termo in n.nome.lower()]
                            if encontrados:
                                print("\nResultados encontrados:")
                                for n in encontrados:
                                    print(n.id, n.nome, n.tipo, n.dureza)
                            else:
                                print("Nenhum material encontrado com esse nome.")
                        elif escolha == "3":
                            id_editar = input("Digite o ID do material que deseja editar: ")
                            materiais = listar_materiais()
                            material = next((n for n in materiais if str(n.id) == id_editar), None)
                            if material:
                                novo_nome = input(f"Novo nome [{material.nome}]: ") or material.nome
                                novo_tipo = input(f"Novo tipo [{material.tipo}]: ") or material.tipo
                                nova_dureza = input(f"Nova dureza [{material.dureza}]: ") or material.dureza
                                atualizar_material(material.id, novo_nome, novo_tipo, int(nova_dureza))
                                print("Material atualizado com sucesso!")
                            else:
                                print("Material não encontrado.")
                        elif escolha == "4":
                            id_excluir = input("Digite o ID do material que deseja excluir: ")
                            materiais = listar_materiais()
                            material = next((n for n in materiais if str(n.id) == id_excluir), None)
                            if material:
                                deletar_material(material.id)
                                print("Material excluído com sucesso!")
                            else:
                                print("Material não encontrado.")
                case "3":
                    while True:
                        print("\n. CLIENTE\n\n1. Cadastrar\n2. Pesquisar\n3. Editar\n4. Excluir\n0. Voltar")
                        escolha = input("Escolha uma opção: ")
                        if escolha == "0":
                            break
                        elif escolha == "1":
                            nome = input("Nome do cliente: ")
                            cpf_cnpj = input("CPF/CNPJ do cliente: ")
                            nome_fantasia = input("Nome fantasia do cliente: ")
                            criar_cliente(nome, cpf_cnpj, nome_fantasia)
                            print("\nClientes cadastrados:")
                            for o in listar_clientes():
                                print(o.id, o.nome, o.cpf_cnpj, o.nome_fantasia)
                        elif escolha == "2":
                            termo = input("Digite o nome (ou parte) do cliente para pesquisar: ").lower()
                            encontrados = [c for c in listar_clientes() if termo in c.nome.lower()]
                            if encontrados:
                                print("\nResultados encontrados:")
                                for c in encontrados:
                                    print(c.id, c.nome, c.cpf_cnpj, c.nome_fantasia)
                            else:
                                print("Nenhum cliente encontrado com esse nome.")
                        elif escolha == "3":
                            id_editar = input("Digite o ID do cliente que deseja editar: ")
                            clientes = listar_clientes()
                            cliente = next((c for c in clientes if str(c.id) == id_editar), None)
                            if cliente:
                                novo_nome = input(f"Novo nome [{cliente.nome}]: ") or cliente.nome
                                novo_cpf_cnpj = input(f"Novo CPF/CNPJ [{cliente.cpf_cnpj}]: ") or cliente.cpf_cnpj
                                novo_nome_fantasia = input(f"Novo nome fantasia [{cliente.nome_fantasia}]: ") or cliente.nome_fantasia
                                atualizar_cliente(cliente.id, novo_nome, novo_cpf_cnpj, novo_nome_fantasia)
                                print("Cliente atualizado com sucesso!")
                            else:
                                print("Cliente não encontrado.")
                        elif escolha == "4":
                            id_excluir = input("Digite o ID do cliente que deseja excluir: ")
                            clientes = listar_clientes()
                            cliente = next((c for c in clientes if str(c.id) == id_excluir), None)
                            if cliente:
                                deletar_cliente(cliente.id)
                                print("Cliente excluído com sucesso!")
                            else:
                                print("Cliente não encontrado.")
                case "4":
                    print("Função de simulação ainda não implementada.")
                case "0":
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida.")

if __name__ == "__main__":
    SistemaGerenciamento().menu_principal()