# Importa bibliotecas
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Realiza leitura de conjunto de dados (dataset)
df = pd.read_csv("https://github.com/TopIntelligence/python_do_zero_a_engenheiro_dados/blob/main/datasets/mtcars.csv")
# Caso queira realizar leitura arquivo Local, trocar a url para o diretório onde está o arquivo, exemplo: D:\Top_Intelligence\Codigos_GitHub\python_do_zero_a_engenheiro_dados\datasets\mtcars.csv

# Verifica dados iniciais
df.head()

# Verifica dados finais
df.tail()

# Verifica quantidade de linhas e colunas
df.shape

# Obtém informações da base de dados
df.info()

# Obtém estatísticas básicas
df.describe()

# Avalia correlação entre as colunas/features
df.corr()

# Pota a correlação de forma gráfica
sns.heatmap(dataframe.corr());