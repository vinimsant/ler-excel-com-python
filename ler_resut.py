# -*- coding: utf-8 -*-
import pandas as pd

list_frase = []
testo = ''
x = 0
tabela = []
nomes = []
notas = []



#ler arquivo
with open('resu_bc.txt') as arquivo:
    texto = arquivo.read()
    
#colocar todo o texto em string
for frase in texto:
    testo += frase

#dividir o texto por inscrição
list_frase = testo.split('/')
   


for palavras in list_frase:
    iten_cortado = palavras.split(',')
    nomes.append(iten_cortado[1])
    notas.append(iten_cortado[6])
    #dicion = {'nome':iten_cortado[1], 'nota':iten_cortado[6]}
    #tabela.append(dicion)
    
        
df = pd.DataFrame({'nome':nomes, 'nota':notas})
df = df.sort_values(by='nota')

df.to_excel(r'C:\Users\e13743a\Documents\vini\script python\rest_bc.xlsx', index=False)

    