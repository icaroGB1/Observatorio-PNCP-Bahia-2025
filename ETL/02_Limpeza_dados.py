#%%
import pandas as pd
# %%
"""
Vou Começar importando os Dados em CSV
"""
pregao = pd.read_csv("../Data/Dados_Brutos/compras_pncpBA6.csv")
dispensa = pd.read_csv("../Data/Dados_Brutos/compras_pncpBA8.csv")
inexigibilidade = pd.read_csv("../Data/Dados_Brutos/compras_pncpBA9.csv") 

# %%
"""
Testando se o import deu certo, gosto de usar o head ou tail por pegar dados  da primeira ou ultima posição
"""
pregao.head()
dispensa.head()
inexigibilidade.head()

"""
Aproveitar para mudar de Pregão eletronico somente para pregão o nome da modalidade 
"""
pregao["modalidadeNome"] = "Pregão"
# %%
"""
Vou Juntar os tipos de modalidade e virar um So dataFrame e fazer a limpeza de forma uniforme sem ser um por um, irei usar axis=0 para empilhar os dataframes, apesar de não ter index eu reset e drop caso tenha 
"""
df = pd.concat([pregao, dispensa, inexigibilidade], axis=0).reset_index(drop=True)

# %%
"""
vou dropar algumas colunas que tem muitos nulls e não irei usar pq para mim não vai ser util para analise 
"""
df.isna().sum()
#%%
"""
Excluindo aqui o que eu não vou usar 
"""
df = df.drop(columns=["linkProcessoEletronico", "emendaParlamentar", "fontesOrcamentarias", "orgaoSubRogado", "unidadeSubRogada", "justificativaPresencial", "linkSistemaOrigem", "usuarioNome" , "informacaoComplementar", "dataAtualizacaoGlobal"])
# %%
"""
Excluindo Colunas redundantes que não vai ter serventias- Tirando as Colunas ID que tem o NOME
"""

df = df.drop(columns=["modalidadeId", "modoDisputaId", "situacaoCompraId", "tipoInstrumentoConvocatorioCodigo"])
# %%
"""
Identifiquei que as colunas ["orgaoEntidade", "unidadeOrgao" e "amparoLegal"] vieram como dicionario irei desmembrar e ver o que vai ser necessário

O ast.literal_eval mudar a String e identifica o dicionario, usei para fazer  novas colunas e tirar o dicionario
"""

import ast 
orgaoEntidade = pd.json_normalize(df["orgaoEntidade"].apply(ast.literal_eval))
unidadeOrgao = pd.json_normalize(df["unidadeOrgao"].apply(ast.literal_eval))
amparoLegal = pd.json_normalize(df["amparoLegal"].apply(ast.literal_eval))  

#%%
"""
Agora vou juntar tudo no dataframe novamente so que de vez de empilhar eu irei colocar ao lado
"""
df = pd.concat([df, orgaoEntidade, unidadeOrgao, amparoLegal], axis=1)
# %%
"""
Irei excluir colunas que não irei usar novamente exemplo a que eu tirei os dicionarios
"""
df = df.drop(columns=["orgaoEntidade", "unidadeOrgao", "amparoLegal", "poderId", "esferaId", "codigoUnidade", "descricao", "codigo"])

# %%
"""
Irei mudar todos os tipos que tem data para o tipo correto
user errors='coerce' devido o valor problemático por NaT
"""
df.dtypes
df["dataAberturaProposta"] = df["dataAberturaProposta"].apply(pd.to_datetime, errors = "coerce")
df["dataInclusao"] = df["dataInclusao"].apply(pd.to_datetime, errors = "coerce")
df["dataEncerramentoProposta"] = df["dataEncerramentoProposta"].apply(pd.to_datetime, errors = "coerce")
df["dataPublicacaoPncp"] = df["dataPublicacaoPncp"].apply(pd.to_datetime, errors = "coerce")
df["dataAtualizacao"] = df["dataAtualizacao"].apply(pd.to_datetime, errors = "coerce")
# %%
df.dtypes
# %%
"""
Verificando dados que não irei usar se tiverem incossistencia irei excluir a linha inteira 

01 - objetoCompra 3 null irei excluir esses 3
02 - Usarei o datase onde somente valorTotalEstimado acima de 0 
03 - Atualizando Ano da Compra que tiveram input errado fiz a retificação e excluir os que estão com o ano errado  - 10 Registro deixando ano somente de 2021 a 2026
04 - tirando compras que passaram de 1 bilhão
"""
df.isnull().sum()
#%%
df = df.dropna(subset=["objetoCompra"])
# %%
df = df[df["valorTotalEstimado"] > 0]
# %%
df.describe()
# %%

df["anoCompra"].value_counts()
df = df[df["anoCompra"].between(2021, 2026)]
# %%
"""
Tratando valor Nulo no valorTotalHomologado
"""
df["valorTotalHomologado"]  = df["valorTotalHomologado"].fillna(0)
# %%
df.isna().sum()
# %%
df.describe()
# %%
df = df[df["valorTotalEstimado"] <= 1_000_000_000]
# %%
"""
Criando Novas Colunas
"""
df["mes_publicacao"] = df["dataPublicacaoPncp"].dt.month
df["ano_mes_publicacao"]= df["dataPublicacaoPncp"].dt.to_period('M')
df["diferenca_valor"] = (df["valorTotalEstimado"] - df["valorTotalHomologado"])

#%%
def porte_compra(x):
    if x < 80000:
        return "Pequena"
    elif x <= 650000:
        return "Média"
    else:
        return "Grande"
def economia (x):
    if(x > 0):
        return True
    else:
        return False
# %%
df["porte_compra"] = df["valorTotalEstimado"].apply(porte_compra)
# %%
df["economia"]= df["diferenca_valor"].apply(economia)
# %%
df.to_csv("dados_limpos_PNCP.CSV")
# %%
df
# %%
