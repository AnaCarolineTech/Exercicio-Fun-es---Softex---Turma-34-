# 1) saudação: imprimir uma mensagem e chamamos a função
def saudacao():
    print("Olá, bem-vindo ao Python!")

saudacao()


# 2) dobro: recebe um número e retorna o dobro
def dobro(n):
    return n * 2

print("dobro(3)  ->", dobro(3))
print("dobro(10) ->", dobro(10))
print("dobro(-4) ->", dobro(-4))


# 3) soma: recebe dois números e retorna a soma
def soma(a, b):
    return a + b

print("soma(10, 20) ->", soma(10, 20))


# 4) mensagem: recebe um nome; se não vier, usa 'visitante'
def mensagem(nome=None):
    if nome:
        print(f"Olá, {nome}!")
    else:
        print("Olá, visitante!")

mensagem("Ana")
mensagem()  # sem nome


# 5) operacoes: retorna soma, subtração e multiplicação
def operacoes(a, b):
    s = a + b
    sub = a - b
    mult = a * b
    return s, sub, mult

res = operacoes(8, 3)
print("operacoes(8,3): soma =", res[0], "| subtração =", res[1], "| multiplicação =", res[2])


# 6) media: aceita quantidade variável de números
def media(*numeros):
    if len(numeros) == 0:
        return 0  # simples: evita divisão por zero
    return sum(numeros) / len(numeros)

print("média de 1,2,3 ->", media(1, 2, 3))                       # 3 valores
print("média de 5,5,5,5,5 ->", media(5, 5, 5, 5, 5))             # 5 valores
print("média de 2,4,6,8,10,12,14 ->", media(2, 4, 6, 8, 10, 12, 14))  # 7 valores


# 7) dados_pessoais: usa **kwargs (chave=valor)
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Ana Caroline", idade=35, cidade="Recife")


# 8) calculadora: tem funções internas e escolhe a operação
def calculadora(operacao, a, b):
    def somar(x, y): return x + y
    def subtrair(x, y): return x - y
    def multiplicar(x, y): return x * y
    def dividir(x, y):
        if y == 0:
            return "Erro: divisão por zero"
        return x / y

    if operacao == "soma":
        return somar(a, b)
    elif operacao == "subtracao":
        return subtrair(a, b)
    elif operacao == "multiplicacao":
        return multiplicar(a, b)
    elif operacao == "divisao":
        return dividir(a, b)
    else:
        return "Operação inválida"

print("calculadora('soma', 10, 5) ->", calculadora("soma", 10, 5))
print("calculadora('divisao', 10, 2) ->", calculadora("divisao", 10, 2))


# 9) aplicar_operacao: recebe dois números e uma função
def aplicar_operacao(a, b, funcao):
    return funcao(a, b)

def soma2(a, b): return a + b
def multiplica2(a, b): return a * b

print("aplicar_operacao(3,4,soma2) ->", aplicar_operacao(3, 4, soma2))
print("aplicar_operacao(3,4,multiplica2) ->", aplicar_operacao(3, 4, multiplica2))
