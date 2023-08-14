#  ===============================================================================
#
#  Autor: Daniel
#  Data: 18/04/2023
#  
#  Objetivo do script:
#  Implementação do Método de Newton-Raphson para encontrar raízes de equações.
#
#  
#  Nome: Newthon-Raphson
#
#
#  Obs: Para o funcionamente correto do script é necessário instalar o módulo do
#  pandas inserindo o comando ' pip install pandas ' no terminal
#
#  ===============================================================================


# ======= #
# Imports #
# ======= #

# Importando a biblioteca pandas para manipulação de dados em formato tabular
import pandas as pd


# ==================== #
# Função a ser iterada #
# ==================== #

# Definindo a função que será iterada
def fdex (x):
    return (x*x*x) - (2*x*x) - 5

def fLinhaDexEmX (x):
    return (3*x*x) - (4*x)


# ================== #
# Entrada de valores #
# ================== #

print ('\n\n\n  ==== Método de Newton-Raphson ====\n')

    
# =================== #
# Valores arbitrários #
# =================== #

# Valores iniciais para os cálculos
xzero = 2.87            # Chute Inicial
kn = 1000               # Número de Iterações
casasDecimais = 4       # Casas decimais a serem arredondadas a cada iteração (1 => par = f'(x), 2=> par = f'(x)/f(x))
tol = 0.001             # Tolerãncia ou erro associado ao método
dig_arred = 1           # Método de arredondamento (1 truncamento, 2 arredondamento ao final do script)
dig_par = 2             # Controla a métrica do calculo do critério de parada


    
# ========= #
# Variáveis #
# ========= #

# Incrementando o número de casas decimais para funcionamento normal do programa
casasDecimais += 1

# Inicialização das tabelas e valores
tabela=[
    ['n'],
    ['xn'],
    ['f(xn)'],
    ['f\'(xn)'],
    ['|f(xn)|'],
]

valores = [
    0,
    float ( str ( xzero )[:str( xzero ).find('.') + casasDecimais] ),
    float ( str( fdex( xzero ))[:str( fdex( xzero ) ).find('.') + casasDecimais] ),
    float ( str( fLinhaDexEmX( xzero ) )[:str( fLinhaDexEmX( xzero )).find('.') + casasDecimais] ),
    float( str( abs( fdex( xzero ) ) )[:str( abs( fdex( xzero ))).find('.') + casasDecimais] ),
]
"""
n[0]\n
xn[1]\n
f_de_xn[2]\n 
f_linha_de_xn[3]\n
modulo_de_f_de_xn[4]\n
"""

# Cálculo de 'par' (Critério de parada) conforme escolha de 'dig_par', determinando um valor inicial para ele
if dig_par == 1:
    par = abs(valores[3]) 

elif dig_par == 2:
    par = abs(valores[3]/valores[4]) 
    tabela.append(['|f(xk)/f\'(xk)|'])
    valores.append (float( str( fdex( valores[1] )/fLinhaDexEmX(valores[1]) )[:casasDecimais]))
    


# ========= #
# Algoritmo #
# ========= #


# Algoritmo principal de Newton-Raphson
while par > tol and valores[0] <= kn:
    
    
    # ======================= #
    # Atualização dos valores #
    # ======================= #
    
    # Atualização da tabela com valores atuais
    for num, itemDaTabela in enumerate(tabela):
       itemDaTabela.append (valores[num])
    
    
    # ========================= # 
    # Redefinição das Variáveis #
    # ========================= #  
    
    # Redefinição das Variáveis conforme escolha de 'dig_arred'
    if dig_arred == 1: # Tirando casas decimais em cada iteração (truncando)
        
        valores[0] += 1
        valores[1] = valores[1] - float( str( fdex( valores[1] )/fLinhaDexEmX( valores[1] ) )[:str( fdex( valores[1] )/fLinhaDexEmX( valores[1] ) ).find('.') +casasDecimais] )
        valores[2] = float( str( fdex( valores[1] ) )[:str( fdex( valores[1] ) ).find('.') + casasDecimais] )
        valores[3] = float( str( fLinhaDexEmX( valores[1] ) )[:str( fLinhaDexEmX( valores[1] ) ).find('.') + casasDecimais] )
        valores[4] = float( str( abs( valores[2] ) )[:str( fLinhaDexEmX( abs( valores[2] ) ) ).find('.') + casasDecimais] )
    
    elif dig_arred == 2: # Arredondando no final do programa
        
        valores[0] += 1
        valores[1] = valores[1] - fdex( valores[1] )/fLinhaDexEmX( valores[1] )
        valores[2] = fdex( valores[1] )
        valores[3] = fLinhaDexEmX( valores[1] )
        valores[4] = abs( valores[2] )
    
    # Cálculo adicional de 'par' conforme escolha de 'dig_par'
    if dig_par == 2:
        valores[5] = float( str( fdex( valores[1] )/fLinhaDexEmX(valores[1]) )[:casasDecimais])
    
    


# ======================= #
# Atualização dos valores #
# ======================= #

# Atualização final da tabela
for num, itemDaTabela in enumerate(tabela):
    itemDaTabela.append (valores[num])


# ================ #
# Saída de valores #
# ================ #

# Criação e formatação do DataFrame
df = pd.DataFrame(tabela).T

df = df.style.set_caption('Newton-Raphson')

# Exportação do DataFrame para um arquivo Excel
while True:
    try:
        df.to_excel('./Newton-Raphson.xlsx')
        print ('\n\n\n  ==== Tabela gerada! ====\n')
        break
    except:
        input ('\nNão é possível sobrescrever o arquivo! Feche o arquivo caso esteja aberto e pressione enter para tentar novamente...\n')
