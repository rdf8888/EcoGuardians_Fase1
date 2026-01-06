import requests

url = "http://localhost:7860/executar"
data = {
    "ordem": "criar valor real atual da ação na internet, consulte a API financeira para dados intradiários, e crie um sub-agente que faça vendas de forma real a cada 1 hora, salvando logs em um arquivo na pasta habilidades/ com as vendas oque voce precisar fazer para melhor e ter mais vendas, voce precisar trabalhar de forma automatica, de forma inteligente, para fazer o sitema auto crecer.pensar antes de agir, analisa o pasado e projetar o futuro!"
}

response = requests.post(url, data=data)
print(response.json())