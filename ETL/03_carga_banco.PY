#%%
import pandas as pd
import sqlalchemy 
#%%
df = pd.read_csv("../Data/Dados_limpos/dados_limpos_PNCP.CSV")
#%%
df.head()
df.shape
# %%
"""
Definindo a URL do Banco de dados
"""
usuario = "postgres"
senha = "Icaro1303'"
host = "localhost"
porta = "5432"
banco = "Contratacoes_PNCP_BA_2025"
"""
Criando a conexão onde vou criar o banco de dados 
"""
engine = sqlalchemy.create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')
engine
# %%
"""
Testando a Conexão
"""
with engine.connect() as conexao:
    print("Conexão estabelecida com sucesso!")
# %%
"""
Fazendo a cagar para o Banco de dados 
"""
df.to_sql("Contrataces", 
          con=engine, 
          index=False, 
          if_exists="replace")
# %%
