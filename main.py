import sys

while True:
    print("Bem-vindo a Calculadora Avançada")
    print("--------------------------------")
    print("Escolha a opção que deseja entrar:")
    print("1- Calculadora de IMC")
    print("2- Calculadora Básica(+,-,*,/)")
    print("0- Sair da Calculadora")

    escolha_opcao = input("Digite a opção que deseja: ")

    if escolha_opcao == '0':
        print("Calculadora encerrada!")
        sys.exit()

    elif escolha_opcao == '1':
        print("Bem-vindo a Calculadora de IMC")
        print("------------------------------")

    # nome do usuário
        nome = input("Qual é o seu nome ? ")
        print("Bem-vindo,", nome, "!")

    # dados do usuário
        peso = float(input("Qual é o seu peso ? "))
        altura = float(input("Qual é a sua altura ? "))

    # calculo do IMC
        imc = peso / (altura ** 2)

    # RESULTADO
        print(f"Seu IMC é : {imc:.2f}")

    # AVALIAÇÃO DO RESULTADO
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

        volta_menu = input("Deseja voltar para o menu? (sim/não): ")

        if volta_menu == 'sim':
            continue

        elif volta_menu == 'não':
            print("Calculadora encerrada")
            sys.exit()

    elif escolha_opcao == '2':
        def soma(x, y):
            return x + y


        def sub(x, y):
            return x - y


        def multi(x, y):
            return x * y


        def div(x, y):
            return x / y


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

            escolha = input("Digite a opção escolhida: ")

            if escolha == '0':
                print("Voltar para o menu")
                break

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
