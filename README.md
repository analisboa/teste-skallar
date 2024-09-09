***************Teste Skallar Digital - Microserviço de Envio de E-mails *******************

Este  é um microserviço simplificado para envio de e-mails utilizando uma API RESTful. Foi utilizado Python com Flask e documentado com Swagger. A API possui testes unitários e permite o envio de e-mails através de uma rota POST.

*********Configuração do Ambiente*******

1. Acessar a documentação da API com Swagger: http://127.0.0.1:5000/docs. 

2. Clone o repositório para sua máquina local.

3. Crie um ambiente virtual para isolar as dependências do projeto.

4. Instale as dependências listadas no arquivo requirements.txt.

5. Crie um arquivo .env na raiz do projeto com as configurações do serviço de e-mail, similar ao modelo abaixo:

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha
EMAIL_USE_TLS=True

6. Com o ambiente configurado, inicie o servidor Flask.

********O microserviço estará rodando no endereço http://127.0.0.1:5000**********

    - Fazer uma requisição POST para a rota /api/send-email: exemplo de payload:

    {
        "to": "destinatario@example.com",
        "subject": "Assunto do E-mail",
        "body": "Corpo do e-mail."
    }



Obrigada, qualquer dúvidas estarei atenta no contato que fizemos por whatsapp.