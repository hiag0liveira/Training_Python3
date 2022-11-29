# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

numero_digitado = input("Digite um numero: ")

if numero_digitado.isdigit():
    numero_digitado_int = int(numero_digitado)
    numero_par_ou_impar = numero_digitado_int % 2 == 0
    numero_par_ou_impar_texto = "ímpar"

    if numero_par_ou_impar:
        numero_par_ou_impar_texto = "par"

    print(f"O número {numero_digitado_int} é {numero_par_ou_impar_texto}")
else:
    print("Você não digitou um número inteiro")

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação apropriada. Ex.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora_digitada = input("Digite a hora em números inteiros: ")

try:
    hora = int(hora_digitada)
    if hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
    else:
        print("Não conheço essa hora")
except:
    print("Por favor, digite apenas números inteiros")


# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

nome_digitado = input("Digite seu nome: ")
tamanho_nome = len(nome_digitado)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Por favor, digite pelo menos mais de uma letra")
