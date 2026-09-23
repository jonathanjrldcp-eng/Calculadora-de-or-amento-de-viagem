# Calculadora-de-or-amento-de-viagem
Este projeto é um programa de terminal desenvolvido em Python para calcular os custos totais de uma viagem e compará-los com o orçamento máximo disponível do cliente. O sistema avalia a viabilidade financeira da viagem e gera um relatório detalhado de gastos.

Funcionalidades
O programa está estruturado em três blocos lógicos principais:

Entrada de Dados: Coleta as informações do cliente, incluindo destino, quantidade de dias, custos fixos (passagem e passeios extras) e custos diários (hospedagem e alimentação), além do orçamento limite.

Processamento de Cálculos: Realiza a totalização das despesas aplicando a fórmula: Custo total = passagem + (diária × dias) + (alimentação × dias) + extras. Em seguida, compara o resultado com o orçamento.

Saída (Relatório): Exibe um extrato no terminal com uma pausa simulada para melhor experiência do usuário (usando a biblioteca time). O relatório informa a classificação do orçamento:

Confortável: Custo menor que o orçamento (exibe quanto sobra).

Apertado: Custo exatamente igual ao orçamento.

Estourado: Custo maior que o orçamento (exibe quanto falta, sem usar números negativos).

Como Executar
Certifique-se de ter o Python 3.x instalado em sua máquina.

Clone ou faça o download do arquivo .py para o seu computador.

Abra o terminal (ou o terminal integrado do VS Code).

Navegue até o diretório onde o arquivo está salvo.

Execute o script com o comando:

Bash
python nome_do_arquivo.py
Insira os dados conforme solicitados pelo terminal. Nota: Para valores decimais em Python, utilize o ponto (.) ao invés de vírgula (ex: 1500.50).

Exemplo de Saída
Plaintext
==== Orçamento ====
Cliente: Maria Silva Destino: Fortaleza
Dias:......... 5
Passagem:..... R$ 800.00
Diária:....... R$ 150.00
Alimentação:.. R$ 100.00
Extras:....... R$ 300.00
Orçamento:.... R$ 3000.00
Custo Total:.. R$ 2350.00
confortavel, sobra R$ 650.00

Tecnologias Utilizadas
Python 3: Linguagem principal do projeto.

Bibliotecas nativas:

time: Utilizada para adicionar o efeito de delay (time.sleep(2)) antes de gerar o recibo final.

os: Importada no escopo para futuras expansões (ex: limpar a tela do terminal).

Autor
Desenvolvido por Jonathan Lopes como resolução de avaliação prática (Programa em Terminal - VS Code).
