import random

line_a = [1,2,3,7,8,9,4,5,6]

#line_a   = [1,2,3,4,5,6,7,8,9]
key = []
def create_line(line_a):
    line, line_b, line_c = [],[],[]
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

def create_collum(master_key):
    lista_2 = []
    key = [2,0,1,5,3,4,8,6,7]
    for x in range(len(key)):
        lista_2.append(master_key[key[x]])
    return lista_2

quadrado2 = create_collum(master_key)
linha2 = create_line(quadrado2)

aux = linha2[1]
linha2[1] = linha2[2]
linha2[2] = aux

quadrado3 = create_collum(quadrado2)

#quadrado3 = tira_quadrado(quadrado3[0])

linha3 = create_line(quadrado3)

aux = linha3[1]
linha3[1] = linha3[2]
linha3[2] = aux

"""print('A B C',linhas)
print('D E F',linha2)
print('G H I',linha3)
"""
"""def formatador():
    for i in range(9):
        if i % 3 == 0:
            print(linha2[0][i],end='')
        else:
            print(linha2[0][i],end='')
formatador()"""
print('+++++++++++++++++++++++++++++++++++++++++++++')
for x in range(len(linhas)):
    print(f'+ _{linhas[x][0]}_|_{linhas[x][1]}_|_{linhas[x][2]}_ || _{linhas[x][3]}_|_{linhas[x][4]}_|_{linhas[x][5]}_ || _{linhas[x][6]}_|_{linhas[x][7]}_|_{linhas[x][8]}_ +')

print('+ = = = = = = = = = = = = = = = = = = = = = +')
for x in range(len(linha2)):
    print(f'+ _{linha2[x][0]}_|_{linha2[x][1]}_|_{linha2[x][2]}_ || _{linha2[x][3]}_|_{linha2[x][4]}_|_{linha2[x][5]}_ || _{linha2[x][6]}_|_{linha2[x][7]}_|_{linha2[x][8]}_ +')

print('+ = = = = = = = = = = = = = = = = = = = = = +')
for x in range(len(linha3)):
    print(f'+ _{linha3[x][0]}_|_{linha3[x][1]}_|_{linha3[x][2]}_ || _{linha3[x][3]}_|_{linha3[x][4]}_|_{linha3[x][5]}_ || _{linha3[x][6]}_|_{linha3[x][7]}_|_{linha3[x][8]}_ +')

print('+++++++++++++++++++++++++++++++++++++++++++++')