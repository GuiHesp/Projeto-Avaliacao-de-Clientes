#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.
# 
# Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.
# 
# Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.
# 
# Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=share_link

# In[1]:


# bibliotecas

import pandas as pd
import numpy as np
import plotly.express as px


# In[2]:


# Importando a base de dados

clientes_df = pd.read_csv(r"clientes.csv", encoding="latin", sep=";")
display(clientes_df)


# In[3]:


# Retirando Coluna Inútil

clientes_df = clientes_df.drop("Unnamed: 8", axis=1) #axis=1 se for coluna
print(clientes_df.info())


# In[4]:


# vendo coluna por possiveis erros

print(clientes_df.dtypes)
print('-'*60)
print(clientes_df.iloc[0])


# In[5]:


# tratando a coluna Salário Anual

clientes_df["Salário Anual (R$)"] = pd.to_numeric(clientes_df["Salário Anual (R$)"], errors="coerce")
print(clientes_df.dtypes)
print('-'*60)
print(clientes_df.iloc[0])


# In[6]:


# Vendo linhas vazias

print(clientes_df.isnull().sum())
#print(clientes_df.info())

# Retirando linhas vazias

clientes_df = clientes_df.dropna()
print(clientes_df.info())


# In[7]:


# Análise Inicial
display(clientes_df.describe()) #mean, para achar o cliente médio

# Cria o gráfico
grafico = px.histogram(clientes_df, x="Origem", y="Nota (1-100)", histfunc="avg", text_auto=True)

# Exibe o gráfico
grafico.show()


# In[8]:


def criar_histograma(tabela, x, y):
    for coluna in clientes_df.columns:
        grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True)
        grafico.show()
        
criar_histograma(clientes_df, x="", y="Nota (1-100)")


# ### Perfil ideal do cliente
#      Acima de 15 anos (dps n se difere tanto)
#      faixa salarial n aparenta fazer mta diferença
#      Entreterimento e artista tem claramente notas melhores (evitar Construção)
#      Tem entre 10 e 15 anos de experiência
#      Com familias não tão grandes, até no max 7 pessoas
