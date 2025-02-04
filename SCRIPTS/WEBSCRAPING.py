import requests
from bs4 import BeautifulSoup

# URL do produto no Mercado Livre
url = "https://www.mercadolivre.com.br/apple-iphone-13-128-gb-estelar-distribuidor-autorizado/p/MLB1018500855#polycard_client=search-nordic&searchVariation=MLB1018500855&wid=MLB3582540395&position=1&search_layout=stack&type=product&tracking_id=f78bef3b-d483-414f-b0d2-83b87ca5ccce&sid=search"

# Enviar uma requisição GET para a URL
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar o elemento que contém o preço
    price_element = soup.find_all('span', {'class': 'andes-money-amount__fraction'})
    
    if price_element:
        # Extrair o texto do elemento
        price = price_element[2].text
        print(f"O preço atual do produto é: R$ {price}")
    else:
        print("Não foi possível encontrar o preço do produto.")
else:
    print(f"Falha ao acessar a página. Status code: {response.status_code}")