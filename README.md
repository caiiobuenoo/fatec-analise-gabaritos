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

### 🧠 Principais Insights (A "Assimetria Controlada")
A análise visual e estatística comprovou que a prova obedece a regras matemáticas estritas de balanceamento e desvio:

* **A Âncora (Letra C):** É a alternativa mais estável de todo o histórico. Ela funciona como o "centro de gravidade" da prova, cravando 10 respostas na maioria absoluta das edições.
* **A Armadilha Estatística (Letra D):** É o fator de volatilidade. Quando a banca projeta uma prova para quebrar os algoritmos de "chute" dos candidatos, ela despeja um volume desproporcional na letra D (registrando picos recordes de até 17 respostas corretas).
* **O Pêndulo Binário (Letra E):** Funciona como variável de compensação de extremos. Ela foge da média central: ou sofre de escassez (8 a 9 respostas) ou inunda o gabarito (atingindo a marca de 14 respostas).

## 🚀 Como reproduzir este projeto
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SeuUsuario/fatec-analise-gabaritos.git](https://github.com/SeuUsuario/fatec-analise-gabaritos.git)
