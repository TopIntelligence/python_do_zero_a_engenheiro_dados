# Importa bibliotecas
import pandas as pd
import numpy as np
import seaborn as sns

# Realiza leitura de conjunto de dados (dataset)
'''
Url do arquivo no Github:
https://github.com/TopIntelligence/python_do_zero_a_engenheiro_dados/blob/main/datasets/mtcars.csv

Atenção:
1- Substitua github.com por raw.githubusercontent.com
2 - Remova a palabra /blob
'''

url = 'D:\\Top_Intelligence\\Codigos_GitHub\\python_do_zero_a_engenheiro_dados\\datasets\\mtcars.csv' # arquivo local
#url = 'D:\Top_Intelligence\Codigos_GitHub\python_do_zero_a_engenheiro_dados\datasets\mtcars.csv' # arquivo local
#url = 'D:/Top_Intelligence/Codigos_GitHub/python_do_zero_a_engenheiro_dados/datasets/mtcars.csv' # arquivo local

#url = 'https://raw.githubusercontent.com/TopIntelligence/python_do_zero_a_engenheiro_dados/main/datasets/mtcars.csv' # arquivo no Github
df = pd.read_csv(url,index_col=0) # Caso queira alguma coluna como index, informar qual através do parâmetro: index_col=0
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
# https://seaborn.pydata.org/generated/seaborn.heatmap.html
sns.heatmap(df.corr());

# Parâmetros
# Parâmetros
# annot=True, fmt="0.1", linewidth=.5, cmap="Spectral", cbar=False
# cores cmap: https://matplotlib.org/stable/tutorials/colors/colormaps.html

sns.heatmap(df.corr(),annot=True, fmt="0.1",linewidth=.5,cmap="tab20b");   

# https://seaborn.pydata.org/generated/seaborn.pairplot.html
sns.pairplot(df) #hue="cyl"