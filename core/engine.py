def generate_board():
    import random
    # Linha base e lista "key" (não utilizada posteriormente)
    line_a, key = [1, 2, 3, 7, 8, 9, 4, 5, 6], []

    def create_line(line_a):
        line, line_b, line_c = [], [], []
        # Linha original
        line.append(line_a)
        # Cria a segunda linha:
        for i in range(6, 9):
            line_b.append(line_a[i])
        for i in range(0, 3):
            line_b.append(line_a[i])
        for i in range(3, 6):
            line_b.append(line_a[i])
        # Cria a terceira linha a partir da segunda:
        for i in range(6, 9):
            line_c.append(line_b[i])
        for i in range(0, 3):
            line_c.append(line_b[i])
        for i in range(3, 6):
            line_c.append(line_b[i])

        line.append(line_b)
        line.append(line_c)
        return line

    linhas = create_line(line_a)

    def tira_quadrado(linhas):
        # Reordena a primeira linha segundo uma chave definida
        chave_linha = [0, 1, 2, 6, 7, 8, 3, 4, 5]
        primeira_linha = linhas[0]
        quadrado = []
        for x in range(len(primeira_linha)):
            quadrado.append(primeira_linha[chave_linha[x]])
        return quadrado

    master_key = tira_quadrado(linhas)

    def create_collum(master_key):
        lista_2 = []
        key = [2, 0, 1, 5, 3, 4, 8, 6, 7]
        for x in range(len(key)):
            lista_2.append(master_key[key[x]])
        return lista_2

    quadrado2 = create_collum(master_key)
    linha2 = create_line(quadrado2)

    # Troca a segunda e terceira linha do bloco para ajuste
    aux = linha2[1]
    linha2[1] = linha2[2]
    linha2[2] = aux

    quadrado3 = create_collum(quadrado2)

    linha3 = create_line(quadrado3)

    aux = linha3[1]
    linha3[1] = linha3[2]
    linha3[2] = aux

    # Constrói o tabuleiro completo (9 linhas)
    board = []
    board.extend(linhas)  # primeiras 3 linhas
    board.extend(linha2)  # próximas 3 linhas
    board.extend(linha3)  # últimas 3 linhas

    return board


def is_valid_sudoku(board):
    valid_set = set(range(1, 10))
    # Verifica as linhas
    for i, row in enumerate(board):
        if set(row) != valid_set:
            print(f"Linha {i + 1} inválida: {row}")
            return False
    # Verifica as colunas
    for i in range(9):
        col = [board[j][i] for j in range(9)]
        if set(col) != valid_set:
            print(f"Coluna {i + 1} inválida: {col}")
            return False
    # Verifica os blocos 3x3
    for block_row in range(3):
        for block_col in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[block_row * 3 + i][block_col * 3 + j])
            if set(block) != valid_set:
                print(f"Bloco na posição ({block_row}, {block_col}) inválido: {block}")
                return False
    return True


def print_board(board):
    # Mantém a estética do output similar ao código original
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    for group in range(3):
        for x in range(3):
            row = board[group * 3 + x]
            print(
                f'+ _{row[0]}_|_{row[1]}_|_{row[2]}_ || _{row[3]}_|_{row[4]}_|_{row[5]}_ || _{row[6]}_|_{row[7]}_|_{row[8]}_ +')
        if group < 2:
            print('+ = = = = = = = = = = = = = = = = = = = = = +')
    print('+++++++++++++++++++++++++++++++++++++++++++++')


# Gera o tabuleiro de Sudoku
board = generate_board()

# Imprime o tabuleiro com a estética original
print_board(board)

# Executa os testes de validação
if is_valid_sudoku(board):
    print("\nO tabuleiro de Sudoku gerado é válido!")
else:
    print("\nO tabuleiro de Sudoku gerado é inválido!")
