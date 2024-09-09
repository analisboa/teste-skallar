import requests

url = "http://localhost:5000/api/send-email"
payload = {
    "to": "testesana19@gmail.com",
    "subject": "Teste de Envio de E-mail",
    "body": "Este é um teste de envio de e-mail. Se eu receber isto, o envio de e-mail está funcionando!"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
