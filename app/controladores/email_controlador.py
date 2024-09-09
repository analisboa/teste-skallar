from flask import request, jsonify
from flask_restx import Resource, fields
from ..services.email_service import EmailService  # Certifique-se de que este caminho está correto
from flask_restx import Namespace

api = Namespace('email', description='Operações de envio de e-mail')

email_model = api.model('Email', {
    'to': fields.String(required=True, description='Endereço de e-mail do destinatário'),
    'subject': fields.String(required=True, description='Assunto do e-mail'),
    'body': fields.String(required=True, description='Conteúdo do e-mail')
})

class EmailController(Resource):
    def __init__(self, *args, **kwargs):
        super(EmailController, self).__init__(*args, **kwargs)
        self.email_service = EmailService()

    @api.expect(email_model)
    @api.response(200, 'E-mail enviado com sucesso.')
    @api.response(500, 'Falha ao enviar o e-mail.')
    def post(self):
        data = request.json
        to = data.get('to')
        subject = data.get('subject')
        body = data.get('body')
        try:
            result = self.email_service.send_email(to, subject, body)
            return {'message': 'E-mail enviado com sucesso'}, 200
        except Exception as e:
            return {'message': f'Falha ao enviar e-mail: {str(e)}'}, 500

    def get(self):
        return jsonify({"message": "GET não implementado para este endpoint"}), 200

api.add_resource(EmailController, '/send-email')
