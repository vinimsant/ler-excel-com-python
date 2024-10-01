import os
from pathlib import Path
import pandas as pd
import pathlib



tabela = list()
tb_final = pd.DataFrame()
#digite o caminho do arquivo
caminho = Path(r'C:\Users\e13743a\Documents\preventiva\relatórios\nf1 feira')
path = list(pathlib.Path(".").glob("*"))

for nome_arquivo in path:
    if(nome_arquivo.suffix == '.xlsx'):
        df=pd.read_excel(nome_arquivo, sheet_name=None)
        df = pd.concat(df)
        tabela.append(df)
        

     
       
for iten in tabela:
    tb_final = pd.concat([tb_final, iten])
    
#digite o caminho onde salvar       
tb_final.to_excel(r"C:\Users\e13743a\Documents\preventiva\relatórios\nf1 feira\tb_teste_nf1.xlsx", index=False)
        

