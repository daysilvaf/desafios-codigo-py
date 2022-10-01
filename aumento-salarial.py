DESAFIO - AUMENTO SALARIAL

A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

--------------------------------------------------
| Salário            | Percentual de Reajuste    |
--------------------------------------------------
| 0 - 600.00         | 17%                       |
--------------------------------------------------
| 600.01 - 900.00    | 13%                       |
--------------------------------------------------
| 900.01 - 1500.00   | 12%                       |
--------------------------------------------------
| 1500.01 - 2000.00  | 10%                       |
--------------------------------------------------
| Acima de 2000.00   | 5%                        |
--------------------------------------------------

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em
percentual.

A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo. 

EXEMPLO 1

-----------------------------------------------------------------------------------------
| Exemplo de Entrada |                              Saída                               |
-----------------------------------------------------------------------------------------
| 1000               | Novo salario: 1120,00 Reajuste ganho: 120,00 Em percentual: 12 % |
-----------------------------------------------------------------------------------------

EXEMPLO 2

-----------------------------------------------------------------------------------------
| Exemplo de Entrada |                              Saída                               |
-----------------------------------------------------------------------------------------
| 2000               | Novo salario: 2200,00 Reajuste ganho: 200,00 Em percentual: 10 % |
-----------------------------------------------------------------------------------------

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar

salario = int(input()) 

if salario <= 600:
  percentual = 17
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 900:
  percentual = 13
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 1500:
  percentual = 12
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 2000:
  percentual = 10
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
else:
  percentual = 5
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
