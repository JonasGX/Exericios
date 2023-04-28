def converte(simbolo):
    dicionario = {'I':1, 'II':2, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    for x in dicionario:
        if simbolo == x:
            return dicionario[simbolo]

def inteiro_para_romano(num):
    # Definir as letras romanas e seus valores correspondentes
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    letras = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    # Inicializar o resultado como uma string vazia
    resultado = ""
    # Loop através dos valores romanos e subtrair do número enquanto ele for maior ou igual ao valor atual
    for i in range(len(valores)):
        while num >= valores[i]:
            num -= valores[i]
            resultado += letras[i]

    print(resultado)

def romano_para_inteiro(s):
    # Criar um dicionário com as letras romanas e seus valores correspondentes
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Inicializar o resultado como zero
    resultado = 0
    # Inicializar o valor da letra anterior como zero
    anterior = 0
    # -1, -1, -1 sempre vai pegar da direita para a esquerda as letras
    for i in range(len(s) - 1, -1, -1):
        # Obter o valor da letra atual
        atual = valores[s[i]]
        print(atual)
        # Se o valor da letra atual for menor do que o valor da letra anterior, subtrair o valor atual do resultado
        if atual < anterior:
            resultado -= atual
        # Caso contrário, adicionar o valor atual ao resultado
        else:
            resultado += atual
        # Atualizar o valor da letra anterior para a próxima iteração
        anterior = atual
    #return resultado
    #return 'mocado'

print(romano_para_inteiro('XLXI'))

# def romano_para_inteiro(s):
#     # Criar um dicionário com as letras romanas e seus valores correspondentes
#     valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     # Inicializar o resultado como zero
#     resultado = 0
#     # Loop através da string romana da direita para a esquerda

#     for i in range(len(s) -1, -1, -1):
#         # Se o valor da letra atual for menor do que o valor da letra anterior, subtrair o valor atual do resultado
#         if i > 0 and valores[s[i]] < valores[s[i - 1]]:
#             print(valores[s[i]])

#             resultado -= valores[s[i]]
#         # Caso contrário, adicionar o valor atual ao resultado
#         else:
#             resultado += valores[s[i]]
#     return resultado
#     #return 'mocado'

