while True:
    print("******************** Programa para calcular o IMC *******************")
    #prova para calcular o imc
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade(anos):"))
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    #calcular o IMC do paciente
    imc = peso / (altura ** 2)
    print("\n==== Resultado ====")
    print(f"nome:{nome}")
    print(f"idade:{idade}")
    print(f"peso:{peso}")
    print(f"altura:{altura}")
            #classificação do imc
    if imc < 18.5:
        print("Abaixo do peso 💪")
    elif imc < 24.9:
        print("Peso normal 💪")
    elif imc < 29.9:
        print("Sobrepeso 🍔")
    elif imc < 34.9:
        print("Obesidade Grau I 🟠")
    elif imc < 39.9:
        print("Obesidade Grau II 🍔")
    elif imc >= 40.0:          
        print("Obesidade Grau III (mórbida) 🚨")
    else:         
        print("gordão")
    continuar = input("deseja calcular o próximo IMC?  (s/n):").lower()
    if continuar !="s":
       print("voce decidiu sair do programa")
       break
      
