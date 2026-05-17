import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("🚀 Carregando dados e gerando o Dashboard Definitivo... Aguarde um momento!")

# =====================================================================
# FASE 1: ENGENHARIA DE DADOS (Dataset Consolidado)
# =====================================================================
dados_brutos = [
    {"Ano_Semestre": "2007.2", "Total": 48, "A": 10, "B": 10, "C": 10, "D": 9, "E": 9},
    {"Ano_Semestre": "2008.1", "Total": 48, "A": 10, "B": 10, "C": 9, "D": 10, "E": 9},
    {"Ano_Semestre": "2009.1", "Total": 48, "A": 10, "B": 11, "C": 9, "D": 9, "E": 9},
    {"Ano_Semestre": "2010.1", "Total": 54, "A": 9, "B": 12, "C": 10, "D": 9, "E": 14},
    {"Ano_Semestre": "2010.2", "Total": 54, "A": 7, "B": 11, "C": 11, "D": 11, "E": 14},
    {"Ano_Semestre": "2011.2", "Total": 54, "A": 11, "B": 11, "C": 14, "D": 10, "E": 8},
    {"Ano_Semestre": "2012.1", "Total": 54, "A": 10, "B": 12, "C": 12, "D": 9, "E": 11},
    {"Ano_Semestre": "2012.2", "Total": 54, "A": 11, "B": 10, "C": 10, "D": 13, "E": 10},
    {"Ano_Semestre": "2013.1", "Total": 54, "A": 11, "B": 12, "C": 9, "D": 12, "E": 10},
    {"Ano_Semestre": "2013.2", "Total": 54, "A": 9, "B": 12, "C": 10, "D": 15, "E": 8},
    {"Ano_Semestre": "2014.1", "Total": 54, "A": 7, "B": 9, "C": 14, "D": 17, "E": 7},
    {"Ano_Semestre": "2014.2", "Total": 54, "A": 9, "B": 11, "C": 10, "D": 10, "E": 14},
    {"Ano_Semestre": "2015.1", "Total": 54, "A": 11, "B": 9, "C": 13, "D": 12, "E": 9},
    {"Ano_Semestre": "2015.2", "Total": 54, "A": 11, "B": 12, "C": 10, "D": 12, "E": 9},
    {"Ano_Semestre": "2016.1", "Total": 54, "A": 9, "B": 8, "C": 17, "D": 12, "E": 8},
    {"Ano_Semestre": "2016.2", "Total": 54, "A": 10, "B": 11, "C": 13, "D": 11, "E": 9},
    {"Ano_Semestre": "2017.1", "Total": 54, "A": 7, "B": 15, "C": 10, "D": 8, "E": 14},
    {"Ano_Semestre": "2017.2", "Total": 54, "A": 9, "B": 12, "C": 10, "D": 11, "E": 12},
    {"Ano_Semestre": "2018.1", "Total": 54, "A": 8, "B": 15, "C": 9, "D": 12, "E": 10},
    {"Ano_Semestre": "2024.1", "Total": 54, "A": 11, "B": 5, "C": 9, "D": 17, "E": 12},
    {"Ano_Semestre": "2024.2", "Total": 54, "A": 8, "B": 5, "C": 10, "D": 17, "E": 14},
    {"Ano_Semestre": "2025.1_A", "Total": 54, "A": 11, "B": 11, "C": 11, "D": 11, "E": 10},
    {"Ano_Semestre": "2025.1_B", "Total": 54, "A": 9, "B": 11, "C": 10, "D": 12, "E": 12},
    {"Ano_Semestre": "2026.1", "Total": 60, "A": 13, "B": 11, "C": 11, "D": 11, "E": 14}
]

df = pd.DataFrame(dados_brutos)
# Grupo de Controle: Isolando as edições padrão de 54 questões
df_moda = df[df['Total'] == 54].copy()

# =====================================================================
# FASE 2: CONFIGURAÇÃO ESTÉTICA E PALETA DE CORES DEFINITIVA
# =====================================================================
sns.set_theme(style="white", font_scale=1.1)

# Definição das cores oficiais do portfólio (Identidade Visual Padrão)
cores_universais = {
    'A': '#1f77b4', # Azul Clássico
    'B': '#ff7f0e', # Laranja
    'C': '#2ca02c', # Verde (A Âncora)
    'D': '#d62728', # Vermelho (A Armadilha)
    'E': '#9467bd'  # Roxo
}

# Criando a estrutura dos subplots (Esquerda: 1 parte | Direita: 2.2 partes de largura)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 8), gridspec_kw={'width_ratios': [1, 2.2]})

# ---------------------------------------------------------------------
# PAINEL 1: O Gabarito Estatístico Ideal (Colunas Verticais Limpas)
# ---------------------------------------------------------------------
gabarito_ouro = {'A': 11, 'B': 12, 'C': 10, 'D': 12, 'E': 9}
lista_cores = [cores_universais[letra] for letra in gabarito_ouro.keys()]

sns.barplot(x=list(gabarito_ouro.keys()), y=list(gabarito_ouro.values()), palette=lista_cores, ax=ax1, edgecolor='black', linewidth=1)
ax1.set_title('O Gabarito Estatístico Ideal (54 Q.)', fontsize=18, fontweight='bold', pad=20)
ax1.set_ylabel('Quantidade de Respostas', fontsize=14)

# Adicionando os números flutuando acima de cada coluna
for i, v in enumerate(gabarito_ouro.values()):
    peso = 'bold' if i in [2, 3] else 'normal' # Destaque em negrito para C e D
    ax1.text(i, v + 0.2, str(v), color='black', ha='center', fontweight=peso, fontsize=15)

# ---------------------------------------------------------------------
# PAINEL 2: Raio-X Histórico (Barras Verticais Empilhadas com Rótulos Internos)
# ---------------------------------------------------------------------
ind = np.arange(len(df_moda))
largura = 0.85
testes = df_moda['Ano_Semestre'].tolist()

bottom = np.zeros(len(df_moda)) # Base zero para iniciar o empilhamento

# Loop para construir o empilhamento letra por letra
for letra in ['A', 'B', 'C', 'D', 'E']:
    valores = df_moda[letra].values
    barras = ax2.bar(ind, valores, largura, bottom=bottom, color=cores_universais[letra], edgecolor='white', linewidth=0.5, label=f'Letra {letra}')
    
    # Escrevendo o número exato bem no centro de cada bloco de cor
    ax2.bar_label(barras, label_type='center', color='white', fontsize=11, fontweight='bold')
    
    bottom += valores # Atualiza o topo para a próxima letra subir a partir dali

ax2.set_title('Raio-X: Gabarito Exato de Cada Vestibular (54 Q.)', fontsize=18, fontweight='bold', pad=20)
ax2.set_ylabel('Total de Questões (0 a 54)', fontsize=14)
ax2.set_xticks(ind)
ax2.set_xticklabels(testes, rotation=45, ha='right')

# Legenda suspensa organizada no canto direito
ax2.legend(title='Alternativas', frameon=True, loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=12)

# ---------------------------------------------------------------------
# FASE 3: ACABAMENTO VISUAL E SALVAMENTO
# ---------------------------------------------------------------------
sns.despine(ax=ax1)
sns.despine(ax=ax2, left=True) # Remove a linha vertical do eixo Y da direita para máxima limpeza

plt.tight_layout()

# Salva o arquivo oficial final na pasta do seu projeto
plt.savefig('gabarito_fatec_definitivo.png', dpi=300, bbox_inches='tight')
plt.show()