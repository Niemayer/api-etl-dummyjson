import requests, json

limit = 10
skip = 0

token = "niemayer_20263976"

headers = {
    "Authorization": f"Bearer {token}"
}

to_valid = True
lista = []
lista_filtro = []

try:
    with open("C:/Users/Niemayer/Documents/project/produtos.json", "w") as produtos:
        while to_valid:
            params = {
                "limit": limit,
                "skip": skip
            }
            response = requests.get("https://dummyjson.com/products", params=params, headers=headers, timeout=5)
            response.raise_for_status()
            dados = response.json()

            for dado in dados['products']:
                produto = {
                    "id": dado["id"],
                    "title": dado["title"],
                    "price": dado["price"],
                    "stock": dado["stock"],
                    "category": dado["category"],
                }
                if produto['price'] > 100 and produto['stock'] < 50:
                    lista_filtro.append(produto)
                else:
                    lista.append(produto)
            skip += limit
            if len(lista) + len(lista_filtro) == dados['total']:
                to_valid = False
        json.dump(lista, produtos)

    with open("C:/Users/Niemayer/Documents/project/produtos_filtrados.json", "w") as produtos_filtrados:
        json.dump(lista_filtro, produtos_filtrados)

except requests.exceptions.ConnectionError:
    print(f"(ConnectionError) Erro de conexão.")
except requests.exceptions.Timeout:
    print(f"(Timeout) Tempo limite excedido.")
except requests.exceptions.HTTPError:
    print(f"(HTTPError) Status: {response.status_code}.")
except requests.exceptions.JSONDecodeError:
    print(f"(JSONDecodeError) Json inválida.")
else:
    print(">>> Dados processados com sucesso.\n")
    print(f"Total disponível na API: {dados['total']}")
    print(f"Total recebido: {len(lista) + len(lista_filtro)}")
    print(f"Total após filtro: {len(lista_filtro)}")
    