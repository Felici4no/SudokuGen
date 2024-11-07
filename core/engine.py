import random

line_a,line,line_b,line_c = [1,2,3,7,8,9,4,5,6],[],[],[]

key = []
def create_line(line_a):
    line.append(line_a)
    #line 2
    for i in range(6,9):
        line_b.append(line_a[i])
    for i in range(0,3):
        line_b.append(line_a[i])
    for i in range(3,6):
        line_b.append(line_a[i])
    #line 3
    for i in range(6,9):
        line_c.append(line_b[i])
    for i in range(0,3):
        line_c.append(line_b[i])
    for i in range(3,6):
        line_c.append(line_b[i])

    line.append(line_b)
    line.append(line_c)
    return line


linhas = create_line(line_a)

def tira_quadrado(linhas):
    chave_linha = [0,1,2,6,7,8,3,4,5]
    primeira_linha = linhas[0]
    quadrado = []
    for x in range(len(primeira_linha)):
        quadrado.append(primeira_linha[chave_linha[x]])
    return quadrado



master_key = tira_quadrado(linhas)
print(master_key)
def create_collum(master_key):
    lista_2 = []
    key = [2,0,1,5,3,4,8,6,7]
    for x in range(len(key)):
        lista_2.append(master_key[key[x]])
    print(lista_2)

quadrado2 = create_collum(master_key)

print(linhas)