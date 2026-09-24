'''CALCULADORA
DE DESPESAS DE VIAGEM – PROGRAMA EM TERMINAL (VS CODE)
2. ENTRADAS (Dados do Cliente)

Nome do cliente
destino
Número de dias (inteiro).
Passagem (ida e volta – valor único).
Diária
da hospedagem (valor por dia).
Gasto médio com alimentação (valor por dia).
Passeios e extras (valor único para a viagem toda).
Orçamento máximo do cliente (valor com centavos).

3.
PROCESSAMENTO (Cálculos)
Custo
total = passagem + (diária × dias) + (alimentação × dias) + extras.
Comparar
o custo total com o orçamento.

Classificar a folga:
Confortável (sobra boa) / Apertado
(sobra pequena) / Estourado (falta dinheiro).

4.
SAÍDA (Resumo para o cliente)
Exibir
todos os valores formatados em R$ com 2 casas decimais.
Informar
se cabe ou não cabe no orçamento.
Mostrar
quanto sobra (se couber) ou quanto falta (se não couber) – nunca exibir valor
negativo.
5.
OBSERVAÇÕES TÉCNICAS

Usar
if / elif / else para a classificação

Comentar
o código em 3 blocos: Entrada, Processamento, Saída.
'''

#AVALIAÇÃO EM DUPLA
#JONATHAN LOPES
import time
import os
nome = input("digite o nome do cliente: ")
destino = input("digite o destino da viagem: ")
dias = int(input("digite o numero de dias da viagem: "))
passagem = float(input("digite o valor da passagem (ida e volta): "))
diaria = float(input("digite o valor da diaria da hospedagem: "))
alimentacao = float(input("digite o valor do gasto medio com alimentacao por dia: "))
extras = float(input("digite o valor dos passeios e extras: "))
orcamento = float(input("digite o valor do orcamento maximo do cliente: "))

custo_total = passagem + (diaria * dias) + (alimentacao * dias) + extras
if custo_total < orcamento:
    sobra = orcamento - custo_total
    print("==== Orçamento ====")
    time.sleep(2)
    print(f"Cliente: {nome} Destino: {destino}")
    print(f"Dias:......... {dias}")
    print(f"Passagem:..... R$ {passagem:.2f}")
    print(f"Diária:....... R$ {diaria:.2f}")
    print(f"Alimentação:.. R$ {alimentacao:.2f}")
    print(f"Extras:....... R$ {extras:.2f}")
    print(f"Orçamento:.... R$ {orcamento:.2f}")
    print(f"Custo Total:.. R$ {custo_total:.2f}")
    print(f"confortavel, sobra R$ {sobra:.2f}")
elif custo_total == orcamento:
    print("==== Orçamento ====")
    time.sleep(2)
    print(f"Cliente: {nome} Destino: {destino}")
    print(f"Dias:......... {dias}")
    print(f"Passagem:..... R$ {passagem:.2f}")
    print(f"Diária:....... R$ {diaria:.2f}")
    print(f"Alimentação:.. R$ {alimentacao:.2f}")
    print(f"Extras:....... R$ {extras:.2f}")
    print(f"Orçamento:.... R$ {orcamento:.2f}")
    print(f"Custo Total:.. R$ {custo_total:.2f}")
    print("apertado, nao sobra dinheiro")
else:
    falta = custo_total - orcamento
    print("==== Orçamento ====")
    time.sleep(2)
    print(f"Cliente: {nome} Destino: {destino}")
    print(f"Dias:......... {dias}")
    print(f"Passagem:..... R$ {passagem:.2f}")
    print(f"Diária:....... R$ {diaria:.2f}")
    print(f"Alimentação:.. R$ {alimentacao:.2f}")
    print(f"Extras:....... R$ {extras:.2f}")
    print(f"Orçamento:.... R$ {orcamento:.2f}")
    print(f"Custo Total:.. R$ {custo_total:.2f}")
    print(f"estourado, falta R$ {falta:.2f}")
