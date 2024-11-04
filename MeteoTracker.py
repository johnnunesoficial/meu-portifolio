import requests  # Biblioteca para fazer requisições HTTP

# Função para obter clima
def obter_clima(cidade):
    # Sua chave de API
    chave_api = '1d0d1eded0191ec9cff2a1b6c4731dc0'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt"
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        umidade = dados['main']['humidity']
        velocidade_vento = dados['wind']['speed']
        
        # Exibindo as informações do clima
        print(f"Clima em {cidade}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Condição: {descricao.capitalize()}")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do Vento: {velocidade_vento} m/s")
    else:
        print(f"Não foi possível obter o clima para a cidade: {cidade}. Verifique se o nome está correto.")

# Prompt para o usuário inserir o nome da cidade
cidade = input("Digite o nome da cidade que você deseja consultar: ")

# Chamada da função
obter_clima(cidade)