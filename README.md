# 🏛️ Observatório PNCP 2025: Análise de Contratações Públicas da BAHIA
📖 Sobre o Projeto

Este projeto surgiu a partir da minha experiência atuando no setor de compras da FUNDAC. Durante esse período, frequentemente me questionava sobre como outros órgãos públicos conduziam seus processos de contratação e quais práticas poderiam servir de referência para aprimorar a gestão das compras públicas e como melhorar internamente.

Com esse interesse, estou desenvolvendo o Observatório PNCP 2025, um projeto de análise de dados voltado para a exploração e consolidação de informações de licitações e contratos públicos disponibilizados pelo Portal Nacional de Contratações Públicas (PNCP).

Para este estudo, foi definido um recorte específico no Estado da Bahia, concentrando a análise exclusivamente nas contratações realizadas por órgãos e entidades públicas baianas ao longo de 2025. Essa abordagem permite uma visão mais detalhada da realidade local, possibilitando identificar padrões, tendências e características das contratações públicas no estado.

Além de promover uma visão mais ampla sobre as compras governamentais, este projeto também teve como objetivo aprofundar meus conhecimentos em Análise de Dados, ETL, consumo de APIs e visualização de informações.

🎯 Objetivo

Realizar uma análise consolidada das contratações públicas realizadas em 2025, identificando padrões, tendências e indicadores relevantes que possam contribuir para a compreensão da eficiência, transparência e competitividade dos processos de compras governamentais.

🔍 Escopo da Análise

>[!IMPORTANT]
Todos os dados analisados neste projeto referem-se exclusivamente a contratações públicas registradas por órgãos e entidades localizados no Estado da Bahia. Portanto, os resultados apresentados não representam o cenário nacional, mas sim um recorte específico das contratações públicas baianas durante o ano de 2025.

A coleta, tratamento e análise dos dados foram concentrados nas modalidades de contratação com maior relevância e volume de utilização na Administração Pública:
*   **Pregão Eletrônico:** Análise da competitividade e economia gerada em processos eletrônicos.
*   **Dispensa de Licitação:** Monitoramento das contratações diretas por valor ou emergência.
*   **Inexigibilidade:** Acompanhamento de contratações de fornecedores exclusivos ou serviços técnicos especializados.

## ⚙️ Pipeline ETL Completo

Este projeto implementa um pipeline ETL (Extract, Transform, Load) robusto para garantir a integridade e a disponibilidade dos dados para análise.

### 1. Extração (Extract) - `ETL/01_coleta_dados.py`
*   **Descrição:** Script Python responsável por consumir a API do Portal Nacional de Contratações Públicas (PNCP) e extrair dados brutos de licitações e contratos. Inclui tratamento de `rate limiting` e `timeouts` para garantir a coleta eficiente.
*   **Tecnologias:** 🐍 Python (Requests).

### 2. Transformação (Transform) - `ETL/02_Limpeza_dados.py`
*   **Descrição:** Script Python que realiza a limpeza, padronização e enriquecimento dos dados brutos. Inclui tratamento de valores nulos, conversão de tipos de dados e desnormalização de campos aninhados (JSON).
*   **Tecnologias:** 🐍 Python (Pandas).

### 3. Carga (Load) - `ETL/03_carga_banco.PY`
*   **Descrição:** Script Python que carrega os dados transformados em um banco de dados PostgreSQL, garantindo a persistência e a estruturação dos dados para futuras consultas e visualizações.
*   **Tecnologias:** 🐍 Python (SQLAlchemy), 🗄️ PostgreSQL.
  
  ## 📊 Próximos Passos: Visualização e Análise

Com o pipeline ETL estabelecido e os dados estruturados no PostgreSQL, os próximos passos incluem:

*   **Criação de Dashboards:** Desenvolvimento de painéis interativos no Power BI para visualização dos principais indicadores e tendências.
*   **Análises Exploratórias:** Realização de análises aprofundadas para identificar anomalias, oportunidades de melhoria e insights estratégicos para a gestão pública.

  ## ✉️ Redes Sociais

*   **LinkedIn:** [in/icaro-gabriel-70a54233b](https://www.linkedin.com/in/icaro-gabriel-70a54233b/ )
*   **Email:** [icarowp45@gmail.com](mailto:icarowp45@gmail.com)
