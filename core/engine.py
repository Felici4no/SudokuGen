import random

line_a,line,line_b,line_c = [1,2,3,7,8,9,4,5,6],[],[],[]

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


print(linhas)