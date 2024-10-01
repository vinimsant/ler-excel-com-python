import os
from pathlib import Path
import pandas as pd



tabela = list()
tb_final = pd.DataFrame()
pasta = os.listdir(r'C:\Users\e13743a\Documents\preventiva\relatórios\nf1 feira')
for i in pasta:
    nome, extecao = os.path.splitext(i)
    if(extecao=='.xlsx'):
        iten = pd.DataFrame(pd.read_excel(i))
        tabela.append(iten) 
       
for iten in tabela:
    tb_final = pd.concat([tb_final, iten])
       
tb_final.to_excel(r"C:\Users\e13743a\Documents\preventiva\relatórios\nf1 feira\tb_final_nf1.xlsx", index=False)
        
