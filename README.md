# 📊 FATEC Exam Analytics: Reverse Engineering & Predictive Modeling

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Manipulation-150458.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Low%20Level%20Rendering-brightgreen.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20API-4C72B0.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success.svg)
![Data Science](https://img.shields.io/badge/Domain-Data%20Science%20%26%20Analytics-black.svg)

## 📌 1. Executive Summary & Business Problem
Testes padronizados de múltipla escolha não são avaliações puramente de conhecimento; eles são sistemas probabilísticos complexos. Para garantir a integridade do exame e mitigar a taxa de sucesso de técnicas baseadas em probabilidade cega (o "chute" estatístico), bancas examinadoras desenvolvem algoritmos proprietários de distribuição de alternativas.

Este projeto aplica técnicas de **Data Analytics, Engenharia Reversa e Estatística Descritiva** sobre duas décadas de histórico (2007 - 2026) do Vestibular da FATEC (Faculdade de Tecnologia de São Paulo). O objetivo primário é auditar a matriz de respostas da banca, identificar os vieses de "Assimetria Controlada" inseridos intencionalmente no sistema e desenvolver uma heurística preditiva para otimização de tomada de decisão em cenários de tempo esgotado.

---

## 🏗️ 2. Arquitetura de Dados e Pipeline ETL
Para garantir a confiabilidade matemática da análise, os dados brutos passaram por um pipeline rigoroso de *Extract, Transform, Load* (ETL):

* **Data Extraction:** Coleta manual/automatizada de espelhos de gabaritos oficiais em formato PDF das edições históricas.
* **Data Wrangling & Transformation:** Normalização de dados não-estruturados em um esquema relacional (DataFrames estruturados no formato Tidy Data).
* **Data Validation (Integrity Checks):** Criação de testes de sanidade garantindo que $\sum (A, B, C, D, E) = Total\_Questions$ para cada registro, eliminando ruídos ou falhas de transcrição.

### 2.1. Cohort Segmentation (Agrupamento Temporal)
O comportamento da banca não é estático; ele evolui. Para evitar contaminação estatística, o *dataset* foi isolado em três *cohorts* de formato de prova:
1. **Cohort Legacy (48 Questões | 2007-2009):** A fase embrionária do exame.
2. **Cohort Standard (54 Questões | 2010-2025):** A "Moda Estatística" e o *core* das nossas análises de variância.
3. **Cohort Expansion (60 Questões | 2026-Atual):** A nova matriz curricular e comportamental da banca.

---

## 📈 3. Dashboard Analítico e Data Visualization

![Dashboard Executivo FATEC](gabarito_fatec_definitivo.png)

A visualização acima utiliza *barplots* estilizados via Seaborn para contrapor o **Modelo de Gabarito Ideal (Média Histórica)** contra o **Raio-X de Frequência Estrita**, permitindo a detecção imediata de *outliers* (pontos fora da curva) na série temporal.

---

## 🔬 4. Deep Dive Analítico: A Psicologia do Algoritmo (Cohort 54Q)
A análise exploratória (EDA) da era de 54 questões permitiu classificar o comportamento de cada alternativa sob a ótica de desvio padrão e risco:

* 🟢 **Letra C (A "Âncora Estatística"):** Atua como o centro de gravidade do modelo e prova de sanidade do exame. Independentemente da volatilidade das outras letras, a Letra C possui o menor Desvio Padrão do conjunto, ancorando-se de forma resiliente na marca de **10 respostas corretas** em mais de 60% da série histórica.
* 🔵 **Letra A (A "Baseline Silenciosa"):** Historicamente discreta, a letra A raramente assume protagonismo. Funciona como um preenchimento seguro e de baixa variância, oscilando em uma banda estreita entre 9 e 11 respostas.
* 🟠 **Letra B (O "Honeypot" Punitivo):** Durante 13 anos, operou como a alternativa de maior volume (11 a 12 pontos). Contudo, a análise de série temporal detectou um *Crash Point* algorítmico nas safras 2024.1 e 2024.2, onde a banca cortou sua presença para **apenas 5 respostas**. Conclusão: a banca rastreia vícios de preenchimento dos candidatos e programa quebras abruptas para punir "chutes" padronizados em opções aparentemente seguras.
* 🔴 **Letra D (O "Gatilho de Caos"):** É o vetor de volatilidade intencional inserido para destruir cálculos de probabilidade lineares. Quando a banca projeta um exame para maximizar a dificuldade probabilística, ela despeja um volume massivo de gabaritos na letra D, registrando picos anômalos que vão de **15 a 17 ocorrências** em um único exame.
* 🟣 **Letra E (O "Pêndulo de Compensação"):** Funciona como a variável dependente do sistema. Como a soma total deve ser obrigatoriamente 54, a Letra E absorve o "troco" das outras alternativas. Isso gera uma distribuição bimodal (binária): ou ela sofre de escassez absoluta (7 a 8 respostas) ou inunda o cartão (atingindo até 14 respostas).

---

## 🔄 5. Evolução Histórica e o Novo Paradigma (60 Questões)
Observando a transição longitudinal:
* **A Era da Simetria (48Q):** Nos primeiros exames, a distribuição beirava a perfeição (10-10-10-9-9). O algoritmo era altamente previsível e vulnerável à engenharia reversa.
* **A Era da Assimetria (54Q):** Introdução das variâncias agressivas (Letras B e D) para quebrar o padrão.
* **A Nova Matriz (60Q - 2026):** O primeiro dado do modelo de 60 questões (A=13, B=11, C=11, D=11, E=14) indica que o algoritmo decidiu congelar o "miolo" da prova. As letras centrais (B, C, D) estão planificadas em 11 ocorrências, enquanto os polos extremos (A e E) passaram a absorver a carga de volatilidade.

---

## 🔮 6. Forecasting: Cenários Preditivos para Otimização de Risco
Transformando dados em inteligência de decisão. Frente ao cenário restrito do vestibular, um candidato deve basear seu *risk management* (gerenciamento de risco) em três cenários de alocação residual:

1. **Cenário Standard (Regressão à Média):** O candidato que precisa preencher lacunas de forma segura deve aportar seu capital de risco na Letra C, devido ao seu comportamento histórico de "Âncora" e baixa volatilidade.
2. **Cenário de Alta Variância (Hedge Contra Punição):** Sabendo que a banca utiliza a letra B como armadilha punitiva recente e a letra D como pico surpresa, distribuições puramente aleatórias nessas alternativas apresentam Risco/Retorno desfavorável.
3. **Cenário Nova Matriz (60 Questões):** Caso a tendência de 2026 se confirme, as letras A e E formam a nova fronteira de segurança, concentrando quase 45% do gabarito total, tornando-se os alvos prediletos para maximização de acertos estatísticos de última hora.

---

## 💻 7. Reproducibilidade & Estrutura do Projeto

### Pré-requisitos (Ambiente de Desenvolvimento)
* Python 3.8+
* Gestão de dependências via `pip` ou ambiente virtual (`.venv` / `conda`).

```bash
# Clone the repository
git clone [https://github.com/caiiobuenoo/fatec-analise-gabaritos.git](https://github.com/caiiobuenoo/fatec-analise-gabaritos.git)

# Navigate to the directory
cd fatec-analise-gabaritos

# Install required Data Science libraries
pip install pandas numpy matplotlib seaborn

# Execute the ETL & Visualization pipeline
python analise_fatec.py
