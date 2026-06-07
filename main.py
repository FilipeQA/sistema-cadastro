# ============================================
# listas para guardar os dados (cap 4)
nomes = []
emails = []
telefones = []
idades = []

# -----------------------------------------------
# funcoes do sistema
# -----------------------------------------------

def mostrar_menu():
    print()
    print("=" * 40)
    print("   BEM VINDO AO SISTEMA DE CADASTRO")
    print("=" * 40)
    print("[1] Cadastrar pessoa")
    print("[2] Listar todos")
    print("[3] Buscar por nome")
    print("[4] Remover cadastro")
    print("[5] Total de cadastros")
    print("[0] Sair")
    print("=" * 40)


def cadastrar():
    print("\n--- NOVO CADASTRO ---")

    nome = input("Digite o nome: ")

    # validacao basica
    if nome == "":
        print("ERRO: nome nao pode ser vazio!")
        return

    # verifica se ja existe (listas)
    if nome in nomes:
        print("Esse nome ja esta cadastrado!")
        return

    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")

    # usando try/except cap 2
    try:
        idade = int(input("Digite a idade: "))
    except:
        print("ERRO: idade tem que ser um numero!")
        return

    if idade < 0 or idade > 120:
        print("ERRO: idade invalida!")
        return

    # adiciona nas listas
    nomes.append(nome)
    emails.append(email)
    telefones.append(telefone)
    idades.append(idade)

    print("\nCadastro realizado com sucesso!! :)")


def listar_todos():
    print("\n--- LISTA DE CADASTROS ---")

    # verifica se tem alguem cadastrado
    if len(nomes) == 0:
        print("Nenhum cadastro encontrado.")
        return

    # loop para mostrar todos - cap 3
    for i in range(len(nomes)):
        print()
        print(f"Cadastro #{i + 1}")
        print(f"  Nome     : {nomes[i]}")
        print(f"  Email    : {emails[i]}")
        print(f"  Telefone : {telefones[i]}")
        print(f"  Idade    : {idades[i]} anos")
        print("-" * 30)


def buscar():
    print("\n--- BUSCA POR NOME ---")

    if len(nomes) == 0:
        print("Nenhum cadastro para buscar.")
        return

    busca = input("Digite o nome para buscar: ")

    encontrou = False

    # percorre a lista procurando o nome
    for i in range(len(nomes)):
        # usei .lower() para nao ter problema com maiusculas/minusculas
        if busca.lower() in nomes[i].lower():
            print()
            print(f">>> ENCONTRADO! (posicao {i + 1})")
            print(f"  Nome     : {nomes[i]}")
            print(f"  Email    : {emails[i]}")
            print(f"  Telefone : {telefones[i]}")
            print(f"  Idade    : {idades[i]} anos")
            print("-" * 30)
            encontrou = True

    if not encontrou:
        print("Nenhum resultado encontrado para:", busca)


def remover():
    print("\n--- REMOVER CADASTRO ---")

    if len(nomes) == 0:
        print("Nenhum cadastro para remover.")
        return

    nome = input("Digite o nome para remover: ")

    # verifica se existe
    if nome not in nomes:
        print("Nome nao encontrado!")
        return

    # pega a posicao na lista
    posicao = nomes.index(nome)

    # confirmacao antes de apagar
    confirma = input(f"Tem certeza que quer remover '{nome}'? (s/n): ")

    if confirma.lower() == "s":
        # remove de todas as listas na mesma posicao
        nomes.pop(posicao)
        emails.pop(posicao)
        telefones.pop(posicao)
        idades.pop(posicao)
        print("Cadastro removido com sucesso!")
    else:
        print("Operacao cancelada.")


def total_cadastros():
    print(f"\nTotal de pessoas cadastradas: {len(nomes)}")

    # so mostra media se tiver alguem
    if len(idades) > 0:
        soma = 0
        for idade in idades:
            soma = soma + idade
        media = soma / len(idades)
        print(f"Media de idade: {media:.1f} anos")


# -----------------------------------------------
# programa principal - aqui comeca tudo
# -----------------------------------------------

print("Carregando sistema...")

# loop principal do programa (cap 3 - while!)
rodando = True

while rodando:
    mostrar_menu()
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar_todos()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        remover()
    elif opcao == "5":
        total_cadastros()
    elif opcao == "0":
        print("\nAte logo! Valeu por usar o sistema :D")
        rodando = False
    else:
        print("Opcao invalida! Tente de novo.")

# fim do programa
