import pandas as pd

# Carregar um dataset CSV como exemplo
df = pd.read_csv("dataset_ic_ufba.csv")

# Exibir as primeiras linhas
print(df.head())




# se precisar puxar do site

# from bs4 import BeautifulSoup
# import requests

# url = "https://www.ic.ufba.br"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # Exemplo: Pegar todos os títulos das notícias do site
# titulos = [h2.text for h2 in soup.find_all("h2")]
# print(titulos)
