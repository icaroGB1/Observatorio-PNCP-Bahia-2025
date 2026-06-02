#%%
import pandas as pd
#%%
"""
Verificando se os DATAFRAME foram importados da forma correta e verificando o nome das modalidade para lidar de forma facil para futuramente o dashboard por tipo de modalidade de quebra mudei de pregão eletronico para Pregão
"""
pregao = pd.read_csv("..\Data/Dados_Brutos/compras_pncpBA6.csv")
pregao.head()
pregao["modalidadeNome"] = "Pregão"

dispensa = pd.read_csv("..\Data/Dados_Brutos/compras_pncpBA8.csv")
dispensa.head()
dispensa["modalidadeNome"]

inexigibilidade = pd.read_csv("../Data/Dados_Brutos/compras_pncpBA9.csv")
inexigibilidade.head()
inexigibilidade["modalidadeNome"]
# %%
"""
Junção das Colunas e reniciei o indice 
"""
df = pd.concat([inexigibilidade, dispensa, pregao], axis=0).reset_index(drop=True)
# %%
"""
Conferindo se a junção das colunas deu tudo certo 
"""
print(df["modalidadeNome"].value_counts())
# %%
"""
Verificando o quantitatide de nulos para começar a excluir as colunas 
"""
df.isna().sum()

# %%
"""
Aqui fiz para verificar o que tem em cada coluna antes de excluir
"""
df["fontesOrcamentarias"].value_counts()

"""
Excluindo colunas que não vou usar 
"""
df = df.drop(columns=['emendaParlamentar', "orgaoSubRogado", "unidadeSubRogada", "justificativaPresencial", "linkProcessoEletronico", "informacaoComplementar", "linkSistemaOrigem", "usuarioNome" , "fontesOrcamentarias",])

# %%
"""
Excluindo colunas redundantes
"""
df = df.drop(columns=["modalidadeId", "modoDisputaId", "situacaoCompraId", "tipoInstrumentoConvocatorioCodigo"])
# %%
df.shape
# 
# %%
import ast

orgao_Entidade = pd.json_normalize(df["orgaoEntidade"].apply(ast.literal_eval))
unidade_Orgao = pd.json_normalize(df["unidadeOrgao"].apply(ast.literal_eval))
amparo_Legal = pd.json_normalize(df["amparoLegal"].apply(ast.literal_eval))
# %%
df = pd.concat([df, orgao_Entidade, unidade_Orgao, amparo_Legal],axis=1)
# %%
df = df.drop(columns=["orgaoEntidade", "unidadeOrgao", "amparoLegal"])
# %%
df
# %%
df.isna().sum()
# %%
df = df.rename(columns={"cnpj": "cnpj_orgao", "razaoSocial": "razaoSocial_orgao", "nome": "nome_amparo"})
#%%
df = df.drop(columns=["codigo", "descricao", "ufNome", "esferaId", "poderId"])
# %%
df.shape
# %%
df["valorTotalHomologado"] = df["valorTotalHomologado"].fillna(0)
#%%
df.isna().sum()
# %%
df.loc[df["objetoCompra"].isna(), ["objetoCompra"]]
df = df.dropna(subset=["objetoCompra"])
# %%
df.dtypes
# %%
df[["dataInclusao", "dataPublicacaoPncp", "dataAtualizacao", "dataAberturaProposta", "dataEncerramentoProposta"]]= df[["dataInclusao", "dataPublicacaoPncp", "dataAtualizacao", "dataAberturaProposta", "dataEncerramentoProposta"]].apply(pd.to_datetime, errors='coerce')
# %%
df.dtypes
# %%
df["mes_publicacao"] = df["dataPublicacaoPncp"].dt.month
# %%
df
# %%
df["diferenca_valor"] = (df["valorTotalEstimado"] - df["valorTotalHomologado"])
# %%
df
# %%
df["percentual_economizado"] = round(df["diferenca_valor"] / df["valorTotalEstimado"] * 100, 2)
# %%
df
# %%
def porte_compra(x):
    if x < 80000:
        return "Pequena"
    elif x <= 650000:
        return "Média"
    else:
        return "Grande"
# %%
df["porte_compra"] = df["valorTotalEstimado"].apply(porte_compra)
# %%
df[df["diferenca_valor"] < 0]
# %%
df.iloc[89987]

# %%
