import requests

def main():
    mensagem = "⚽ Bot de Apostas: Possível entrada detectada!"
    
    bot_token = '7823093640:AAFJeuAeYP3CHvlsY5vFScNpg1g3nfNGsD4'
    chat_id = '7823093640'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    data = {
        'chat_id': chat_id,
        'text': mensagem
    }
    
    response = requests.post(url, data=data)
    print("Status:", response.status_code)
    print("Resposta:", response.text)

if name == "__main__":
    main()
