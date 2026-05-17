# 📊 Engenharia Reversa de Gabaritos: Análise Estatística do Vestibular FATEC

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Manipulation-150458.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data%20Visualization-brightgreen.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plotting-4C72B0.svg)

## 🎯 O Desafio
Será que as bancas de vestibulares e concursos distribuem as alternativas corretas de forma puramente aleatória, ou existem vieses metodológicos e algoritmos ocultos de "Assimetria Controlada"? 

Este projeto de **Data Analytics** explora o histórico de gabaritos do Vestibular da FATEC (Faculdade de Tecnologia do Estado de São Paulo) das edições de 2007 a 2026. O objetivo foi extrair, limpar e analisar dados estruturados de dezenas de provas para identificar padrões de estabilidade, volatilidade extrema e compensação matemática.

## 🛠️ Metodologia e Pipeline de Dados
1. **Coleta de Dados:** Extração de dados históricos de arquivos PDF de gabaritos oficiais.
2. **ETL (Extract, Transform, Load):** - Normalização dos dados em formato tabular.
   - **Isolamento do "Grupo de Controle":** filtragem estrita das edições que seguem o padrão exato de 54 questões (a "Moda" estatística do exame) para garantir comparabilidade perfeita sem distorções proporcionais.
3. **Análise Exploratória de Dados (EDA):** Mapeamento de frequências, análise de distribuição horizontal e projeção estatística de um modelo ideal utilizando Python (`Pandas`, `Matplotlib` e `Seaborn`).

## 📈 Dashboard e Resultados

![Dashboard Fatec](gabarito_fatec_definitivo.png)

### 🧠 Principais Insights (O Padrão de Cada Alternativa)
A análise visual e estatística comprovou que a prova obedece a regras matemáticas estritas de balanceamento e desvio. Cada alternativa possui um papel específico na arquitetura do exame:

* **Letra A (A Base Silenciosa):** Historicamente discreta, a letra A raramente é protagonista (picos altos) ou vilã (escassez extrema). Ela atua como um preenchimento seguro, flutuando em uma banda muito estreita e previsível, geralmente estacionando entre 9 e 11 respostas.
* **Letra B (A Falsa Segurança):** Durante mais de uma década, comportou-se como a alternativa mais forte da prova (cravando 11 a 12 pontos). Porém, os dados revelam que recentemente a banca alterou seu algoritmo: nas edições de 2024.1 e 2024.2, a letra B sofreu um corte drástico, despencando para apenas 5 respostas corretas, provando que os examinadores ativamente punem chutes viciados.
* **Letra C (A Âncora Estatística):** É o "centro de gravidade" da prova. Independentemente de quão caótica a distribuição se torne nas outras letras, a C é a alternativa que apresenta a maior resiliência histórica, cravando frequentemente o valor exato de 10 respostas corretas na maioria absoluta das edições.
* **Letra D (A Armadilha de Volatilidade):** É o fator de caos desenhado pela banca. Quando o exame é projetado para quebrar os cálculos de probabilidade dos candidatos, um volume desproporcional de respostas corretas é despejado na letra D, que já registrou os maiores picos da história do exame (atingindo a marca de 17 respostas).
* **Letra E (O Pêndulo de Compensação):** Funciona como a variável de ajuste matemático para fechar as 54 questões. Por ser usada para equilibrar o exame, ela foge da média central: apresenta um comportamento binário onde ou sofre de extrema escassez (7 a 8 respostas) ou inunda o gabarito (atingindo 14 respostas).

## 🚀 Como reproduzir este projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/caiiobuenoo/fatec-analise-gabaritos.git
