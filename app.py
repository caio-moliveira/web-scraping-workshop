import requests


url = "https://www.mercadolivre.com.br/apple-iphone-16-pro-max-1-tb-titnio-preto-distribuidor-autorizado/p/MLB1040287854#polycard_client=search-nordic&wid=MLB5093482120&sid=search&searchVariation=MLB1040287854&position=9&search_layout=stack&type=product&tracking_id=57cfe630-205e-426a-8b31-18eb4ed9ccc6"
response = requests.get(url)
print(response)