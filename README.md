# Projeto de Geração de Tabuleiro com Estrutura de Linhas e Colunas

Este projeto em Python utiliza a manipulação de listas e funções para gerar e formatar um tabuleiro estruturado em blocos 3x3, semelhante a um quebra-cabeça ou jogo de Sudoku.

## Descrição do Código

O código realiza as seguintes operações principais:

1. **Definição da Linha Inicial (`line_a`)**: A lista `line_a` define a sequência inicial de números de 1 a 9, que serve como base para a criação de linhas e colunas organizadas.
2. **Função `create_line()`**: Esta função cria três linhas baseadas em uma linha inicial. Cada nova linha é uma reorganização da linha anterior para simular uma estrutura 3x3.
3. **Função `tira_quadrado()`**: Extrai uma nova sequência da linha inicial, ordenando-a de acordo com a chave `chave_linha` para formar um "quadrado" ou sequência reordenada.
4. **Função `create_collum()`**: Reordena os elementos da sequência extraída para formar uma coluna reorganizada, com base na chave `key`.
5. **Geração e Exibição do Tabuleiro**: O tabuleiro final é exibido em um formato visual estruturado para representar as linhas e colunas em blocos 3x3.

## Exemplo de Uso

O código ao final do script gera o tabuleiro formatado e exibe no console com a seguinte estrutura:

```
+++++++++++++++++++++++++++++++++++++++++++++
+ _1_|_2_|_3_ || _7_|_8_|_9_ || _4_|_5_|_6_ +
+ _7_|_8_|_9_ || _4_|_5_|_6_ || _1_|_2_|_3_ +
+ _4_|_5_|_6_ || _1_|_2_|_3_ || _7_|_8_|_9_ +
+ = = = = = = = = = = = = = = = = = = = = = +
+ _3_|_1_|_2_ || _9_|_7_|_8_ || _6_|_4_|_5_ +
+ _9_|_7_|_8_ || _6_|_4_|_5_ || _3_|_1_|_2_ +
+ _6_|_4_|_5_ || _3_|_1_|_2_ || _9_|_7_|_8_ +
+ = = = = = = = = = = = = = = = = = = = = = +
+ _2_|_3_|_1_ || _8_|_9_|_7_ || _5_|_6_|_4_ +
+ _8_|_9_|_7_ || _5_|_6_|_4_ || _2_|_3_|_1_ +
+ _5_|_6_|_4_ || _2_|_3_|_1_ || _8_|_9_|_7_ +
+++++++++++++++++++++++++++++++++++++++++++++
```

## Estrutura de Arquivo

- `line_a`: Sequência inicial de números de 1 a 9.
- Funções:
  - `create_line(line_a)`: Cria as linhas principais.
  - `tira_quadrado(linhas)`: Reorganiza uma linha para criar uma nova sequência.
  - `create_collum(master_key)`: Reordena a sequência para formar uma coluna.
- `linhas`, `linha2`, `linha3`: Estruturas de linhas formatadas para o tabuleiro final.
  
## Como Executar

Execute o código em um ambiente Python 3 para gerar e visualizar o tabuleiro formatado. 

```bash
python tabuleiro.py
```

## Requisitos

- Python 3.x
