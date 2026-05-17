import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import pi
from matplotlib.lines import Line2D

print("💎 Gerando o Painel Triplo Master 2.0 (Acessibilidade e Rigor Acadêmico)...")

# =====================================================================
# FASE 1: DADOS
# =====================================================================
dados_brutos = [
    {"Ano_Semestre": "2007.2", "A": 10, "B": 10, "C": 10, "D": 9, "E": 9},
    {"Ano_Semestre": "2008.1", "A": 10, "B": 10, "C": 9, "D": 10, "E": 9},
    {"Ano_Semestre": "2009.1", "A": 10, "B": 11, "C": 9, "D": 9, "E": 9}
]

df_long = pd.DataFrame(dados_brutos).melt(id_vars=['Ano_Semestre'], 
                                          value_vars=['A', 'B', 'C', 'D', 'E'], 
                                          var_name='Alternativa', value_name='Frequência')

df_wide = pd.DataFrame(dados_brutos).set_index('Ano_Semestre')[['A', 'B', 'C', 'D', 'E']]

# =====================================================================
# FASE 2: ENGENHARIA VISUAL E ACESSIBILIDADE
# =====================================================================
sns.set_theme(style="whitegrid", font_scale=1.1)

# Título Global Corporativo "amarrando" os três gráficos
fig = plt.figure(figsize=(24, 8.5))
plt.suptitle('FATEC Analytics: Cohort Legacy (48 Questões) — Engenharia Reversa e Padrões de Previsibilidade', 
             fontsize=20, fontweight='bold', color='#1a1a1a', y=0.98)

cores_universais = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# ---------------------------------------------------------------------
# PAINEL 1: O Muro Simétrico (Frequência Absoluta)
# ---------------------------------------------------------------------
ax1 = fig.add_subplot(131)

# Removida a legenda automática para usar a legenda customizada abaixo
sns.barplot(data=df_long, x='Ano_Semestre', y='Frequência', hue='Alternativa', 
            palette=cores_universais, edgecolor='black', linewidth=0.8, ax=ax1)
if ax1.get_legend() is not None:
    ax1.get_legend().remove()

for container in ax1.containers:
    ax1.bar_label(container, padding=3, fontsize=11, fontweight='bold', color='#333333')

ax1.axhline(y=9.6, color='#333333', linestyle='--', linewidth=2)
ax1.set_title('Distribuição por Edição (Frequência Absoluta)', fontsize=15, fontweight='bold', pad=15, color='#333333')
ax1.set_xlabel('Edição do Vestibular', fontsize=13, labelpad=10)
ax1.set_ylabel('Quantidade de Respostas Corretas', fontsize=13, labelpad=10)
ax1.set_ylim(0, 13)

# Legenda Centralizada e Limpa no Rodapé
man_A = Line2D([0], [0], color=cores_universais[0], marker='s', linestyle='None', label='Letra A')
man_B = Line2D([0], [0], color=cores_universais[1], marker='s', linestyle='None', label='Letra B')
man_C = Line2D([0], [0], color=cores_universais[2], marker='s', linestyle='None', label='Letra C')
man_D = Line2D([0], [0], color=cores_universais[3], marker='s', linestyle='None', label='Letra D')
man_E = Line2D([0], [0], color=cores_universais[4], marker='s', linestyle='None', label='Letra E')
man_avg = Line2D([0], [0], color='#333333', linestyle='--', linewidth=2, label='Média Teórica Perfeita (9.6Q)')

ax1.legend(handles=[man_A, man_B, man_C, man_D, man_E, man_avg], 
           title="Ativos de Dados & Referências", loc='upper center', 
           bbox_to_anchor=(0.5, -0.16), ncol=3, frameon=True, fontsize=11)

# ---------------------------------------------------------------------
# PAINEL 2