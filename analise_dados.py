import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregamento e Preparação dos Dados
df_linux = pd.read_csv('benchmark_resultados_Linux.csv')
df_windows = pd.read_csv('benchmark_resultados_Windows.csv')

# Identificação dos ambientes (Atualizado para CachyOS)
df_linux['Sistema'] = 'CachyOS (Linux)'
df_windows['Sistema'] = 'Windows 11'

# Unir os dataframes
df = pd.concat([df_linux, df_windows], ignore_index=True)

# Calcular o tempo total de cada iteração
df['total_ms'] = df['alloc_ms'] + df['write_ms'] + df['read_ms'] + df['free_ms']

# 2. Configuração Visual e Geração dos Gráficos
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análise Comparativa de Desempenho de Memória: Windows vs Linux', fontsize=16)

# Gráfico A: Tempo Total
sns.boxplot(ax=axes[0, 0], data=df, x='bloco_MB', y='total_ms', hue='Sistema', palette='Set1')
axes[0, 0].set_title('A. Distribuição do Tempo Total de Operação por Bloco')
axes[0, 0].set_xlabel('Tamanho do Bloco (MB)')
axes[0, 0].set_ylabel('Tempo Total (ms)')

# Gráfico B: Tempo de Escrita
sns.lineplot(ax=axes[0, 1], data=df, x='bloco_MB', y='write_ms', hue='Sistema', marker='o', palette='Set1')
axes[0, 1].set_title('B. Tempo Médio de Escrita (Evolução)')
axes[0, 1].set_xlabel('Tamanho do Bloco (MB)')
axes[0, 1].set_ylabel('Tempo de Escrita (ms)')

# Gráfico C: Tempo de Alocação
sns.barplot(ax=axes[1, 0], data=df, x='bloco_MB', y='alloc_ms', hue='Sistema', palette='pastel')
axes[1, 0].set_title('C. Tempo Médio de Alocação de Memória')
axes[1, 0].set_xlabel('Tamanho do Bloco (MB)')
axes[1, 0].set_ylabel('Tempo de Alocação (ms)')

# Gráfico D: Tempo de Liberação
sns.barplot(ax=axes[1, 1], data=df, x='bloco_MB', y='free_ms', hue='Sistema', palette='pastel')
axes[1, 1].set_title('D. Tempo Médio de Liberação de Memória')
axes[1, 1].set_xlabel('Tamanho do Bloco (MB)')
axes[1, 1].set_ylabel('Tempo de Liberação (ms)')

plt.tight_layout()
# Salva com um novo nome para refletir a alteração
plt.savefig('graficos_comparativos_cachyos.png', dpi=300)
plt.show()