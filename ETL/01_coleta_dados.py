#%%
import requests
import pandas as pd
import time
"""
Definindo as variaves que irei usar para consumir a API
"""
modalidade = {"Pregão":6, "Dispensa": 8, "inexigibilidade":9}
uf = "BA"
pag = 1
data_inicial = '20250101'
data_final = '20251231'
# %%
"""
Criação do LOOP para extração
"""
def extract (modalidade, uf:str, pag:int, data_inicial:str , data_final:str):
    dados = []
    url = "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial={data_inicial}&dataFinal={data_final}&codigoModalidadeContratacao={modalidade}&uf={uf}&pagina={pag}&tamanhoPagina=50"
    session = requests.Session()
    session.headers.update({
       "User-Agent": "ConsumindoAnalisedeDados/1.0 (icarowp45@gmail; PNCP)",
    "Accept": "application/json",
    "Referer": "https://pncp.gov.br/"
    })
    for i in modalidade:    
        dados.clear()
        pag = 1 
        while True:
            try:
                respostas = session.get(url.format(data_inicial = data_inicial, data_final = data_final, modalidade = modalidade[i],uf=uf, pag = pag),timeout=30)
                if(respostas.status_code == 200):
                    dados_atual = respostas.json()
                    total_pag = int(dados_atual["totalPaginas"])
                    dados.extend(dados_atual["data"])
                    print(f"{i} — Página {pag}/{total_pag}")
                    pag+=1
                    if(pag > total_pag):
                        break
                    time.sleep(1.5)
                elif (respostas.status_code == 422 or respostas.status_code == 400):
                    print ("Erro:", respostas.json())
                    time.sleep(1.5)
                else:
                    print(respostas.status_code)
                    break 
            except requests.exceptions.ReadTimeout:
                print("Tempo Excedido")
                time.sleep(2)
            except requests.exceptions.ConnectionError:
                print("Erro de conexão")
                time.sleep(5)
            except Exception as e:
                print(f"erro inesperado{e}")
                time.sleep(10)
        df = pd.DataFrame(dados)
        df.to_csv(f'compras_pncp{uf}{modalidade[i]}.csv',encoding='utf-8', index=False)
        print(f"{i} concluído — {len(df)} registros salvos")

# %%
extract(modalidade, uf, 1, data_inicial,data_final)


# %%
