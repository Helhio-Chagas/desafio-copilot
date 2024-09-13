# Repete uma string um determinado número de vezes.

def repetir_string(texto, vezes):

  # Utilizando o método * para repetir a string

  string_repetida = texto * vezes
  return string_repetida

# Obtendo a entrada do usuário

string_original = input("Digite a string: ")
numero_repeticoes = int(input("Digite o número de repetições: "))

# Chamando a função e imprimindo o resultado

resultado = repetir_string(string_original, numero_repeticoes)
print(resultado)