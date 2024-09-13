# Realiza as quatro operações matemáticas básicas entre dois números.

def calculadora(num1, num2):

  # Realizando as operações
  soma = num1 + num2
  subtracao = num1 - num2
  multiplicacao = num1 * num2
  divisao = num1 / num2  # Assumindo que o usuário não irá dividir por zero

  # Imprimindo os resultados
  print("A soma é:", soma)
  print("A subtração é:", subtracao)
  print("A multiplicação é:", multiplicacao)
  print("A divisão é:", divisao)

# Obtendo os números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chamando a função
calculadora(numero1, numero2)