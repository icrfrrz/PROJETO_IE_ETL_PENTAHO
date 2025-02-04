import requests
from bs4 import BeautifulSoup
import pandas as pd

# Configurar pandas para exibir todas as linhas
pd.set_option('display.max_rows', None)

df = pd.read_excel('D:\dataset_administradora.xlsx')

# Filtrar os dados onde nm_administradora começa com "AFFIX"
filtered_df = df[df['contrato.nm_administradora'].str.startswith('AFFIX')]

# Exibir todas as colunas e linhas do DataFrame filtrado
print(filtered_df)