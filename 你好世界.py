print("Hello World")
'''
faturamento = 1200 
custo = 700
novas_vendas = 100
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.10
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento 
print('faturamento foi: ', faturamento)
print('custo foi de: ', custo) 
print('o valor de imposto foi de: ', imposto)
print('o lucro foi de: ', lucro)
print('a margem de lucro foi de: ', round(margem_lucro, 2))
tempo_contrato = 170
tempo_ano = 170 / 12
print('tempo em ano: ', int(tempo_ano))
tempo_mes = 170 % 12
print('tempo em mes: ', tempo_mes)
faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print(f"faturamento da empresa: {faturamento}, custo: {custo}, lucro:{lucro}")

email_cliente = "qualquer@gmail.com"

#maiuscula - toda a string
email_cliente = email_cliente.upper()

#minuscula - toda a string
email_cliente = email_cliente.lower()

#encontrar "@" - localizar a posicao do indice do caracter
print(email_cliente.find("@")) #se aparecer -1, e igual a nao encontrado - erro

#tamanho do texo
print(len(email_cliente)) 

#selecionar um elemento da string
print(email_cliente[0]) # 0 = q, 8 = @

#selecionar uma parte da string
print(email_cliente[:])

#trocar os elementos do texto
novo_email = email_cliente.replace("gmail.com", "icloud.com")
print(novo_email)

nome = "john colt"
print(nome.capitalize()) # somente o primeiro caracter de toda a string) em maiuscula
print(nome.title()) # primeiro caracter de toda palavra da string

#extrair elemento da string de forma dinaminca
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

#pegar o primeiro nome
position_espace = nome.find(" ")
first_name = nome[:position_espace]
print(first_name)

#pegar o sobrenome
last_name = nome[position_espace + 1:]
print(last_name)

#casos especiais - formatacao numerica em texto
margem_lucro = round(margem_lucro, 2)
print(f"faturamento da empresa: R${faturamento:.2f}, custo: R${custo:.2f}, lucro: R${lucro:.2f}, margem: {margem_lucro:.0%}") 
'''
'''
#INPUT 
email = input("Escreva o seu email: ")
nome = input("Seu primeiro nome: ")

print(nome, email)

print(f"{nome}, verifique seu email: {email} que enviamos um link de confirmacao")

faturamento = float(input("Escreva o faturamento: "))
imposto = faturamento * 0.1
print(imposto)
'''
'''
#LISTA
vendas = [100, 50, 14 , 60, 80, 700]

#soma dos elementos da lista 
total_vendas = sum(vendas)

#tamanho da lista 
quantidade_vendas = len(vendas)

#max e min
print(max(vendas))
print(min(vendas))

#localizar o indice de uma lista
print(vendas[1])

lista_produtos = ["iphone", "airpod", "ipad", "imac"]
#produto_procurado = produto_procurado.lower()

#print(produto_procurado in lista_produtos)

#adiconar um item na lista
lista_produtos.append("macbook")

#removar um item da lista
lista_produtos.remove("macbook") #string 
lista_produtos.pop(3) #indice

#editar um item da lista
precos = [1000, 1500, 3500]
precos[0] = 4000  #ou precos[0] = procos[0] * 1.5

#contar quantidade de item que aparece na lista 
lista_produtos = ["iphone", "airpod", "ipad", "imac", "ipad", "imac", "imac"]
print(lista_produtos.count("imac"))

#ordenar uma lista
lista_produtos.sort() #ordem alfabetica ou crescente(num)
lista_produtos.sort(reverse=True) #ordem alfabetica contraria ou decrescente(num)
'''
'''
#IF - ELSE - ELIF
if condicao/comparacao:
    #se for true, executa aqui
else:
    #se for false, executa aqui
condicoes <, >, <=, >=, ==, != 
 and(E) e or(OU)
vendas = 1500
metas = 1400

if vendas > metas:
    print("meta alcancado, ganha bonus")
    bonus = 0.1 *vendas
    print(f"bonus ganhos: {bonus}")
else:
    print("meta nao atingido")


vendas = 150
meta1 = 130 # +10%
meta2 = 170 # +15%

if vendas >= meta2:
    bonus = vendas * 0.15
elif vendas >= meta1:
    bonus = vendas * 0.1
else:
    bonus = 0
print("Bonus ganhos: ", bonus)


lista_produtos = ["iphone", "airpod", "ipad", "imac"]
produto_procurado = input("procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("produto em estoque")
else: 
    print("nao encontrado no estoque")
'''
'''
##FOR 
lista_vendas = [1000, 500, 800, 1500, 2000, 2300]

meta = 1700
percentual_bonus = 0.1 

 # para CADA elemento da LIST
for item in lista_vendas:
    if item > meta:
        bonus = percentual_bonus * item
    else:
        bonus = 0
    print(bonus)
'''
'''
##dicionario
dic_produto = {"airpod": 2000, "ipad": 6000, "iphone": 5000, "imac":13000}

#selecionar um elemento
print(dic_produto["airpod"])

#editar um elemento
dic_produto["airpod"] = dic_produto["airpod"] * 1.4
print(dic_produto)

#quantidade de elemento no dicionario
print(len(dic_produto))

#retirar um elemento
dic_produto.pop("airpod")
print(dic_produto)

#adicionar um elemento
dic_produto["apple watch"] = 2700
print(dic_produto)

#verificar se um elemento existe no dicionario
if "iphone" in dic_produto:
    print("existe produto")
else:
    print("nao existe")

#verifique se um valor existe nos valores do dicionario
if 6000 in dic_produto.values():
    print("Existe")
else:
    print("Nao existe")


nome_produto = input("nome do produto: ")
proco_produto = float(input("preco do produto: "))

nome_produto = nome_produto.lower()

dic_produto[nome_produto] = proco_produto

print(dic_produto)


for produto in dic_produto:
    novo_proco = dic_produto[produto] * 1.1
    dic_produto[produto] = novo_preco

print(dic_produto)
'''
