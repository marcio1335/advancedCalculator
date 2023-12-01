import sys

# Apresentação inicial do programa
print("Bem-vindo ao Sistema de Cadastro")
print("--------------------------------")

# Dicionário para armazenar usuários e senhas
usuarios = {}

# Variável de controle para autenticação
autenticado = False

# Loop principal enquanto o usuário não estiver autenticado
while not autenticado:

    # Menu de opções
    print("Escolha a opção: ")
    print("1 - Novo Usuário")
    print("2 - Usuário Cadastrado")
    print("0 - Sair")

    # Solicitação da escolha do usuário
    escolha = input("Digite a opção: ")

    # Opção para cadastrar novo usuário
    if escolha == '1':
        print("Seja bem-vindo, vamos realizar o cadastro!")

        # Solicitação de dados para novo usuário
        usuario = input("Digite o usuário que deseja cadastrar: ")

        # Loop para garantir uma senha de 4 dígitos
        while True:
            try:
                senha = int(input("Digite 4 números para a senha: "))
                if len(str(senha)) == 4:
                    break
                else:
                    print("A senha deve ter exatamente 4 números. Tente novamente.")
            except ValueError:
                print("Por favor, digite apenas números.")

        # Armazena usuário e senha no dicionário
        usuarios[usuario] = senha
        print(f"Usuário {usuario} cadastrado com sucesso!")

    # Opção para login de usuário existente
    elif escolha == '2':
        # Verifica se há usuários cadastrados
        if not usuarios:
            print("Nenhum usuário cadastrado. Por favor, cadastre um usuário primeiro.")
            continue

        print("Insira os dados para efetuar o login: ")
        usuario_login = input("Usuário: ")
        senha_login = input("Senha: ")

        # Verifica se usuário e senha coincidem
        if usuario_login in usuarios and senha_login == str(usuarios[usuario_login]):
            print("Login feito com sucesso!")
            print("------------------------")
            print(f"Seja bem-vindo, {usuario_login}!")

            # Loop para as opções da Calculadora Avançada
            while True:
                print("Bem-vindo a Calculadora Avançada")
                print("--------------------------------")
                print("Escolha a opção que deseja entrar:")
                print("1- Calculadora de IMC")
                print("2- Calculadora Básica(+,-,*,/)")
                print("3 - Conversor de Unidades Básicas")
                print("0- Sair da Calculadora")

                # Solicitação da escolha da calculadora
                escolha_opcao = input("Digite a opção que deseja: ")

                # Opção para sair da Calculadora
                if escolha_opcao == '0':
                    print("Calculadora encerrada!")
                    sys.exit()

                # Opção para Calculadora de IMC
                elif escolha_opcao == '1':
                    print("Bem-vindo a Calculadora de IMC")
                    print("------------------------------")

                    # Solicitação do nome do usuário
                    nome = input("Qual é o seu nome ? ")
                    print("Bem-vindo,", nome, "!")

                    # Solicitação de dados para o cálculo do IMC
                    peso = float(input("Qual é o seu peso ? "))
                    altura = float(input("Qual é a sua altura ? "))

                    # Cálculo do IMC
                    imc = peso / (altura ** 2)

                    # Apresentação do resultado do IMC
                    print(f"Seu IMC é : {imc:.2f}")

                    # Avaliação do resultado do IMC
                    if imc < 16.9:
                        print("Seu IMC está muito abaixo do peso.")
                    elif 17.0 <= imc < 18.4:
                        print("Seu IMC está abaixo do peso.")
                    elif 18.5 <= imc < 24.9:
                        print("Seu IMC está normal.")
                    elif 25.0 <= imc < 29.9:
                        print("Seu IMC está acima do peso.")
                    elif 30.0 <= imc < 34.9:
                        print("Seu IMC está em obesidade grau I.")
                    elif 35.0 <= imc < 40.0:
                        print("Seu IMC está em obesidade grau II.")
                    elif imc >= 40.0:
                        print("Seu IMC está em obesidade grau III.")

                    # Opção para voltar ao menu
                    volta_menu = input("Deseja voltar para o menu? (sim/não): ")

                    # Se desejar voltar, continua o loop, senão encerra o programa
                    if volta_menu == 'sim':
                        continue
                    elif volta_menu == 'não':
                        print("Calculadora encerrada")
                        sys.exit()

                # Opção para Calculadora Básica
                elif escolha_opcao == '2':
                    # Funções para operações básicas
                    def soma(x, y):
                        return x + y

                    def sub(x, y):
                        return x - y

                    def multi(x, y):
                        return x * y

                    def div(x, y):
                        return x / y

                    # Loop para as operações básicas
                    while True:
                        print("Escolha a operação:")
                        print("----------------------")
                        print("1 - Soma")
                        print("2 - Subtração")
                        print("3 - Multiplicação")
                        print("4 - Divisão")
                        print("----------------------")
                        print("0 - Voltar para o menu")
                        print("----------------------")

                        # Solicitação da escolha da operação
                        escolha = input("Digite a opção escolhida: ")

                        # Opção para voltar ao menu
                        if escolha == '0':
                            print("Voltar para o menu")
                            break

                        # Execução da operação escolhida
                        elif escolha in ('1', '2', '3', '4'):
                            num1 = float(input("Digite um número: "))
                            num2 = float(input("Digite outro número: "))

                            if escolha == '1':
                                print(f"{num1} + {num2} = {soma(num1, num2)}")
                            elif escolha == '2':
                                print(f"{num1} - {num2} = {sub(num1, num2)}")
                            elif escolha == '3':
                                print(f"{num1} * {num2} = {multi(num1, num2)}")
                            elif escolha == '4':
                                print(f"{num1} / {num2} = {div(num1, num2)}")

                        else:
                            print("Opção inválida! Tente outra.")

                # Opção para Conversor de Unidades Básicas
                elif escolha_opcao == '3':
                    # Loop para o Conversor de Unidades Básicas
                    while True:
                        print('----- Conversor de Unidades Básicas -----')
                        print('1 - Conversor de Peso')
                        print('2 - Conversor de Tempo')
                        print('3 - Conversor de Distância')
                        print('4 - Conversor de Velocidade')
                        print('0 - Sair do Conversor')

                        # Solicitação da escolha do tipo de conversor
                        escolha_conversor = input('Digite a opção que deseja acessar: ')

                        # Opção para sair do Conversor
                        if escolha_conversor == '0':
                            print('Você saiu do Conversor')
                            break

                        # Opções para cada tipo de conversor
                        elif escolha_conversor in ('1', '2', '3', '4'):
                            # Opções do Conversor de Peso
                            if escolha_conversor == '1':
                                print('----- Conversor de Peso -----')
                                print('1 - Kg para g')
                                print('2 - Kg para mg')
                                print('3 - g para Kg')
                                print('4 - g para mg')
                                print('5 - mg para Kg')
                                print('6 - mg para g')
                                print('0 - Voltar')

                                # Solicitação da escolha da conversão de peso
                                escolha_peso = input('Digite a opção: ')

                                # Opção para voltar ao menu
                                if escolha_peso == '0':
                                    continue

                                # Execução da conversão de peso escolhida
                                elif escolha_peso in ('1', '2', '3', '4', '5', '6'):
                                    if escolha_peso == '1':
                                        num1 = float(input("Digite o peso em Kg que deseja converter: "))
                                        resultado1 = num1 * 1000
                                        print(f'{num1}kg em g =', resultado1)

                                    elif escolha_peso == '2':
                                        num1 = float(input("Digite o peso em Kg que deseja converter: "))
                                        resultado2 = num1 * 1000000
                                        print(f'{num1}kg em mg =', resultado2)

                                    elif escolha_peso == '3':
                                        num1 = float(input("Digite o peso em g que deseja converter: "))
                                        resultado3 = num1 / 1000
                                        print(f'{num1}g em kg =', resultado3)

                                    elif escolha_peso == '4':
                                        num1 = float(input("Digite o peso em g que deseja converter: "))
                                        resultado4 = num1 * 1000
                                        print(f'{num1}g em mg =', resultado4)

                                    elif escolha_peso == '5':
                                        num1 = float(input("Digite o peso em mg que deseja converter: "))
                                        resultado5 = num1 / 1000000
                                        print(f'{num1}mg em Kg =', resultado5)

                                    elif escolha_peso == '6':
                                        num1 = float(input("Digite o peso em mg que deseja converter: "))
                                        resultado6 = num1 / 1000
                                        print(f'{num1}mg em g =', resultado6)

                            # Opções do Conversor de Tempo
                            elif escolha_conversor == '2':
                                print('----- Conversor de Tempo -----')
                                print('1 - Hora para minuto')
                                print('2 - Hora para segundo')
                                print('3 - Minuto para hora')
                                print('4 - Minuto para segundo')
                                print('5 - Segundo para hora')
                                print('6 - Segundo para minuto')
                                print('0 - Voltar')

                                # Solicitação da escolha da conversão de tempo
                                escolha_tempo = input('Digite a opção: ')

                                # Opção para voltar ao menu
                                if escolha_tempo == '0':
                                    continue

                                # Execução da conversão de tempo escolhida
                                elif escolha_tempo in ('1', '2', '3', '4', '5', '6'):
                                    if escolha_tempo == '1':
                                        num1 = float(input("Digite o tempo em horas que deseja converter: "))
                                        resultado1 = num1 * 60
                                        print(f'{num1}h em min =', resultado1)

                                    elif escolha_tempo == '2':
                                        num1 = float(input("Digite o tempo em horas que deseja converter: "))
                                        resultado2 = num1 * 360
                                        print(f'{num1}h em s =', resultado2)

                                    elif escolha_tempo == '3':
                                        num1 = float(input("Digite o tempo em minutos que deseja converter: "))
                                        resultado3 = num1 / 60
                                        print(f'{num1}min em h =', resultado3)

                                    elif escolha_tempo == '4':
                                        num1 = float(input("Digite o tempo em minutos que deseja converter: "))
                                        resultado4 = num1 * 60
                                        print(f'{num1}min em s =', resultado4)

                                    elif escolha_tempo == '5':
                                        num1 = float(input("Digite o tempo em segundos que deseja converter: "))
                                        resultado5 = num1 / 3600
                                        print(f'{num1}s em h =', resultado5)

                                    elif escolha_tempo == '6':
                                        num1 = float(input("Digite o tempo em segundos que deseja converter: "))
                                        resultado6 = num1 / 60
                                        print(f'{num1}s em min =', resultado6)

                                    # Verifica se a escolha do usuário é '4', indicando a opção do conversor de velocidade.
                                    elif escolha_conversor == '4':
                                        # Exibe o menu do Conversor de Velocidade.
                                        print('----- Conversor de Velocidade -----')
                                        print('1 - Quilômetro/h para metros/s')
                                        print('2 - Quilômetro/h para pés/s')
                                        print('3 - Metro/s para quilômetros/h')
                                        print('4 - Metro/s para pés/s')
                                        print('5 - Pés/s para quilômetros/h')
                                        print('6 - Pés/s para metros/s')
                                        print('0 - Voltar')
                                    
                                        # Solicita ao usuário que digite a opção desejada para a conversão de velocidade.
                                        escolha_velocidade = input('Digite a opção: ')
                                    
                                        # Verifica se o usuário deseja voltar ao menu principal.
                                        if escolha_velocidade == '0':
                                            continue
                                    
                                        # Verifica se a escolha do usuário é válida.
                                        elif escolha_velocidade in ('1', '2', '3', '4', '5', '6'):
                                            # Realiza a conversão de velocidade com base na escolha do usuário.
                                            if escolha_velocidade == '1':
                                                # Converte quilômetros por hora para metros por segundo.
                                                num1 = float(input("Digite a velocidade em quilômetros/h que deseja converter: "))
                                                resultado1 = num1 / 3.6
                                                print(f'{num1}km/h em m/s =', resultado1)
                                    
                                            elif escolha_velocidade == '2':
                                                # Converte quilômetros por hora para pés por segundo.
                                                num1 = float(input("Digite a velocidade em quilômetros/h que deseja converter: "))
                                                resultado2 = num1 / 1.097
                                                print(f'{num1}km/h em ft/s =', resultado2)
                                    
                                            elif escolha_velocidade == '3':
                                                # Converte metros por segundo para quilômetros por hora.
                                                num1 = float(input("Digite a velocidade em metros/s que deseja converter: "))
                                                resultado3 = num1 * 3.6
                                                print(f'{num1}m/s em km/h =', resultado3)
                                    
                                            elif escolha_velocidade == '4':
                                                # Converte metros por segundo para pés por segundo.
                                                num1 = float(input("Digite a velocidade em metros/s que deseja converter: "))
                                                resultado4 = num1 * 3.281
                                                print(f'{num1}m/s em ft/s =', resultado4)
                                    
                                            elif escolha_velocidade == '5':
                                                # Converte pés por segundo para quilômetros por hora.
                                                num1 = float(input("Digite a velocidade em pés/s que deseja converter: "))
                                                resultado5 = num1 * 1.097
                                                print(f'{num1}ft/s em km/h =', resultado5)
                                    
                                            elif escolha_velocidade == '6':
                                                # Converte pés por segundo para metros por segundo.
                                                num1 = float(input("Digite a velocidade em pés/s que deseja converter: "))
                                                resultado6 = num1 / 3.281
                                                print(f'{num1}ft/s em m/s =', resultado6)


            autenticado = True  # Altera a variável de controle
        else:
            print("Usuário ou senha incorretos.")

    elif escolha == '0':
        print("Saindo do Sistema de Cadastro. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
