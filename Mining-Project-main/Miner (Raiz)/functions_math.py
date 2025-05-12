from sympy import symbols, solve, Eq, And

# Entrada de dados
Me = float(input("Digite o valor da Meta de extração: "))
Lt = float(input("Digite o valor do tempo limite: "))
X = float(input("Digite a eficiência da escavadeira em m³/h (X): "))
Y = float(input("Digite a eficiência da perfuratriz em m³/h (Y): "))

CL = int(input("Escolha uma das opções:\n1 - Custo\n2 - Lucro\n3 - Ambos\n4 - Nenhum\n"))

if CL != 1 and CL != 2 and CL != 3 and CL != 4:
    print("Opção inválida. Por favor, escolha uma opção válida.")
    exit()

if CL == 1:
    Ceh = float(input("Digite o custo da escavadeira: "))
    Cp = float(input("Digite o custo da perfuratriz: "))
    Cehp = Ceh + Cp
if CL == 2:
    Leh = float(input("Digite o lucro da escavadeira: "))
    Lp = float(input("Digite o lucro da perfuratriz: "))
    Lehp = Leh + Lp
if CL == 3:
    Ceh = float(input("Digite o custo da escavadeira: "))
    Cp = float(input("Digite o custo da perfuratriz: "))
    Cehp = Ceh + Cp
    
    Leh = float(input("Digite o lucro da escavadeira: "))
    Lp = float(input("Digite o lucro da perfuratriz: "))
    Lehp = Leh + Lp
    

# Definir variáveis simbólicas
Xeh, Yp = symbols('Xeh Yp')

# Reformular inequações como equações auxiliares
# Substituir Xeh e Yp por suas expressões simbólicas
Xeh_real = X * Xeh
Yp_real = Y * Yp
if CL == 1 or CL == 3:
    Xeh_custo = Ceh * Xeh
    Yp_custo = Cp * Yp
if CL == 2 or CL == 3:
    Xeh_lucro = Leh * Xeh
    Yp_lucro = Lp * Yp

# Criar equações auxiliares para os limites
eq1 = Eq(Xeh + Yp, Lt)  # Aproximação para resolver o limite de tempo
eq2 = Eq(Xeh_real + Yp_real, Me)  # Aproximação para resolver a meta de extração
if CL == 1:
    eq3 = Eq(Xeh_custo + Yp_custo, 0)  # Aproximação para resolver o custo total
if CL == 2:
    eq3 = Eq(Xeh_lucro + Yp_lucro)  # Aproximação para resolver o lucro total
if CL == 3:
    eq3 = Eq(Xeh_custo + Yp_custo, 0)  # Aproximação para resolver o custo total
    eq4 = Eq(Xeh_lucro + Yp_lucro)  # Aproximação para resolver o lucro total
# Resolver o sistema de equações
if CL == 4:
    solucao = solve([eq1, eq2], (Xeh, Yp))
    Xeh_valor = solucao[Xeh]
    Yp_valor = solucao[Yp]
if CL == 1:
    solucao = solve([eq1, eq2, eq3], (Xeh, Yp))
    if solucao == []:
        solucao = solve([eq1, eq2], (Xeh, Yp))
        Xeh_valor = solucao[Xeh]
        Yp_valor = solucao[Yp]
        Custo = (Xeh_valor * Ceh) + (Yp_valor * Cp)
    else:
         Xeh_valor = solucao[Xeh]
         Yp_valor = solucao[Yp]
   
if CL == 2:
    solucao = solve([eq1, eq2, eq3], (Xeh, Yp))
    if solucao == []:
        solucao = solve([eq1, eq2], (Xeh, Yp))
        Lucro = eq3
        Xeh_valor = solucao[Xeh]
        Yp_valor = solucao[Yp]
    else:
         Xeh_valor = solucao[Xeh]
         Yp_valor = solucao[Yp]
if CL == 3:
    solucao = solve([eq1, eq2, eq3, eq4], (Xeh, Yp)) 
    if solucao == []:
        solucao = solve([eq1, eq2], (Xeh, Yp))
        Custo = eq3
        Lucro = eq4
        Xeh_valor = solucao[Xeh]
        Yp_valor = solucao[Yp]
    else:
        Xeh_valor = solucao[Xeh]
        Yp_valor = solucao[Yp]
    
    


print(f"A quantidade de Escavadeira tem que ser de: {Xeh_valor}")
print(f"A quantidade de Perfuratrizes tem que ser de: {Yp_valor}")

# Exibir a solução
print("A quantidade de Escavadeiras e Perfuratrizes que satisfazem as condições são: ", Xeh_valor, "para as escavadeiras e ", Yp_valor, " para as perfuratrizes.")

if CL == 1:
    print(f"O custo total é: {Custo}")
if CL == 2:
    print(f"O lucro total é: {Lucro}")
if CL == 3:
    print(f"O custo total é: {Custo}")
    print(f"O lucro total é: {Lucro}")

    # Resolver o sistema de equações com as condições
if CL == 4:
    solucao2 = solve([eq1, eq2], (Xeh > 0 , Yp > 0))
if CL == 1:
    solucao2 = solve([eq1, eq2, eq3], (Xeh > 0 , Yp > 0))
if CL == 2:
    solucao2 = solve([eq1, eq2, eq3], (Xeh > 0 , Yp > 0))
if CL == 3:
    solucao2 = solve([eq1, eq2, eq3, eq4], (Xeh > 0 , Yp > 0))

    # Verificar se há solução válida
if (solucao2):
    Xeh_valor = solucao2[0][Xeh]
    Yp_valor = solucao2[0][Yp]
    
    print("Para que a quantidade de Escavadeiras e Perfuratrizes sejam positivas, temos: ")

    print(f"O valor de Xeh é: {Xeh_valor}")
    print(f"O valor de Yp é: {Yp_valor}")

    # Exibir a solução
    print("A quantidade de Escavadeiras e Perfuratrizes que satisfazem as condições são: ", Xeh_valor, "para as escavadeiras e ", Yp_valor, "para as perfuratrizes.")

else:
    print("Não há solução válida onde a quantidade de Escavadeiras e Perfuratrizes sejam positivas.")
