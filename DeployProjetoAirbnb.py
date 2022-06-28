#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import streamlit as st
import joblib

x_numericos = {'Latitude': 0, 'Longitude': 0, 'Quantas Pessoas Acomoda': 0, 'Quantidade de Banheiros': 0,
               'Quantidade de Quartos': 0, 'Quantidade de Camas': 0, 'Valor Adicional por Pessoa Extra': 0,
               'Mínimo de Noites': 0, 'Ano': 0, 'Mês': 0, 'Quantidade de Comodidades': 0,
               'Quantidade de Anúncios do Proprietário no Airbnb': 0}

x_tf = {'Bom Proprietário (baseado nas avaliações do Airbnb)': 0, 'Reserva Imediata': 0}

x_listas = {'Tipo de Propriedade': ['Apartamento', 'Cama e Café da Manhã', 'Condomínio', 'Suíte de Hóspedes',
            'Casa de Hóspedes', 'Hotel', 'Casa', 'Loft', 'Outros', 'Apartamento de Serviço'],
            'Tipo de Quarto': ['Inteiro Casa/Apto', 'Quarto de Hotel', 'Quarto Privado', 'Quarto Compartilhado'],
            'Política de Cancelamento': ['Flexível', 'Moderada', 'Rigorosa', 'Rigorosa com 14 dias de Carência']
            }

dicionario = {}
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0

        
st.image('Logotipo Imobiliário.png', width= 250)
st.title('Modelo de Previsão')
st.markdown('''## 
**Objetivo:** *Construir um modelo de previsão de preço que permita uma pessoa comum
que possui um imóvel possa saber quanto deve cobrar pela diária do seu imóvel.
Ou ainda, para o locador comum, dado o imóvel que ele está buscando,
ajudar a saber se aquele imóvel está com preço atrativo
(abaixo da média para imóveis com as mesmas características) ou não.*

**Obs:** *O modelo só será eficaz com imóveis localizados no Rio de Janeiro.*

''')
st.text('\n')
st.text('\n')
st.text('\n')
        
for item in x_numericos:
    if item == 'Latitude' or item == 'Longitude':
        valor = st.number_input(f'{item}',step=0.00001, value=0.0, format='%.5f')
    elif item == 'Pessoa Extra':
        valor = st.number_input(f'{item}',step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}',step=1, value=0)
    x_numericos[item] = valor
    
for item in x_tf:
    valor = st.selectbox(f'{item}',('Sim','Não'))
    if valor == 'Sim':
        x_tf[item] = 1
    else:
        x_tf[item] = 0
        
for item in x_listas:
    valor = st.selectbox(f'{item}',x_listas[item])
    dicionario[f'{item}_{valor}'] = 1
    
botao = st.button('Prever Valor do Imóvel', help= 'Clique Para Prever')

with st.spinner('Carregando!'):
    if botao:
        dicionario.update(x_numericos)
        dicionario.update(x_tf)
        valores_x = pd.DataFrame(dicionario,index=[0])
        modelo = joblib.load('modelo.joblib')
        preco = modelo.predict(valores_x)
        st.header(f'R${str(preco[0])}')    

