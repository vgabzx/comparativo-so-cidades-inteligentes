Reprodução do Microbenchmark: Windows 11 vs Linux (CachyOS)

Este repositório contém os scripts em Python utilizados para comparar o tempo de execução de operações de memória (alocação, escrita, leitura e liberação) entre os ambientes Windows 11 e CachyOS. O experimento faz parte da avaliação da disciplina de Programação para Ciência de Dados (UniJuí).

💻 Pré-requisitos e Ambiente

* Hardware Base: Notebook Dell (16 GB de RAM disponível).
* Interpretador: Python 3.12.10 estritamente instalado em ambos os sistemas.
* Bibliotecas de Análise: pandas, matplotlib, seaborn.

📂 Estrutura de Arquivos

benchmark_os.py: Script principal que executa o microbenchmark e gera os dados brutos.
analise_dados.py: Script responsável por consolidar os CSVs, calcular as médias e gerar os gráficos comparativos.
benchmark_resultados_Windows.csv / benchmark_resultados_Linux.csv: Dados brutos coletados durante o experimento (1000 registros cada).
graficos_comparativos_cachyos.png: Resultado visual gerado pela análise de dados.

🚀 Instruções de Execução do Benchmark

Para garantir o rigor do experimento, reinicie a máquina, faça o boot no sistema operacional desejado e aguarde rigorosamente 5 minutos antes de iniciar a execução para estabilização dos processos em segundo plano.

1. No Windows 11
Abra o Prompt de Comando (CMD), navegue até a pasta do projeto e execute invocando a versão correta do Python:

cmd
py -3.12 benchmark_os.py

2. No Linux (CachyOS)
Abra o Terminal, navegue até a pasta do projeto. Edite o arquivo benchmark_os.py e certifique-se de que a última linha esteja configurada para rodar_benchmark("Linux"). Em seguida, execute:

python benchmark_os.py

(Nota: Certifique-se de que o comando python no seu CachyOS está apontando para a versão 3.12.10 usando ferramentas como o pyenv, se necessário).

📊 Geração da Análise e Gráficos
Após coletar os dois arquivos .csv gerados pelo benchmark, certifique-se de que eles estão na mesma pasta que o script de análise.

Abra o terminal ou CMD e instale as dependências visuais, caso não as tenha:

pip install pandas matplotlib seaborn

Execute o script de análise de dados:

python analise_dados.py

O console imprimirá a tabela com as médias de tempo por bloco e sistema, e o arquivo graficos_comparativos_cachyos.png será gerado automaticamente na mesma pasta.