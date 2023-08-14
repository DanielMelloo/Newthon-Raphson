# Método de Newton-Raphson para Encontrar Raízes de Equações

Este script implementa o Método de Newton-Raphson para encontrar raízes de equações. O objetivo é encontrar um valor aproximado de uma raiz da função fornecida através de iterações.

## Funções Matemáticas

As funções a serem usadas neste script são definidas da seguinte forma:

- Função Original: `f(x) = x^3 - 2x^2 - 5`
- Derivada da Função: `f'(x) = 3x^2 - 4x`

## Entrada de Valores

- `xzero`: Valor inicial para o cálculo da raiz.
- `kn`: Número máximo de iterações.
- `casasDecimais`: Número de casas decimais a serem arredondadas a cada iteração.
- `tol`: Tolerância ou erro associado ao método.
- `dig_arred`: Método de arredondamento (1 para truncamento, 2 para arredondamento ao final do script).
- `dig_par`: Controle da métrica para cálculo do critério de parada.

## Algoritmo

1. Inicialização dos valores iniciais e configurações.
2. Cálculo da métrica de parada `par` de acordo com `dig_par`.
3. Iterações utilizando o Método de Newton-Raphson até que a métrica de parada seja menor que a tolerância ou o número máximo de iterações seja atingido.
4. Atualização dos valores a cada iteração, incluindo o cálculo de `par` se `dig_par` for 2.
5. Armazenamento dos valores em uma tabela.
6. Exportação dos resultados para um arquivo Excel.

## Utilização

1. Defina os valores iniciais e as configurações desejadas no início do script.
2. Execute o programa.
3. O programa irá iterar usando o Método de Newton-Raphson e armazenar os resultados em uma tabela.
4. Ao final das iterações, os resultados serão exportados para um arquivo Excel chamado "Newton-Raphson.xlsx".

## Requisitos

- Pandas: Biblioteca para manipulação de dados em formato tabular.

## Estrutura do Projeto

|- newton_raphson.py
|- Newton-Raphson.xlsx (gerado automaticamente)


## Autores

- [@/DanielMelloo](https://github.com//DanielMelloo) - Autor original do script

## Feedback

Se você tiver algum feedback ou precisar de suporte, fique à vontade para entrar em contato através do email: danielmello.dev@gmail.com

---
