import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"


def buscar_noticias(categoria="technology", idioma="en", quantidade=20):
    params = {
        "category": categoria,
        "language": idioma,
        "pageSize": quantidade,
        "apikey": API_KEY
    }

    resposta = requests.get(BASE_URL, params=params)
    dados = resposta.json()

    artigos = dados.get("articles", [])

    noticias = []
    for artigo in artigos:
        # Adicionar cada notícia à lista de notícias, extraindo as informações relevantes
        #append é um método de lista que adiciona um item ao final da lista. Neste caso, estamos adicionando um dicionário com as informações relevantes de cada artigo à lista de notícias.
        noticias.append({
            # Processar cada artigo e extrair as informações relevantes
            "titulo": artigo.get("title", ""),
            "descricao": artigo.get("description", ""),
            "fonte": artigo.get("source", {}).get("name", ""),
            "publicado_em": artigo.get("publishedAt", "")
        })
        
    return pd.DataFrame(noticias)

if __name__=="__main__":
    df = buscar_noticias()
    print(df.head())
    df.to_csv("noticias.csv", index=False)
    print("Noticias salvas em noticias.csv")
    
