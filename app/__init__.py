from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)

    # Defina o caminho da documentação do Swagger
    api = Api(app, version='1.0', title='API de Envio de Emails',
              description='Documentação da API para envio de emails',
              doc='/docs')  # Rota para a documentação do Swagger

    # Aqui você adiciona os namespaces
    from app.controladores.email_controlador import api as email_ns
    api.add_namespace(email_ns, path='/api')

    return app
