from flask_restx import Namespace, Resource, fields
from ..controladores.email_controlador import EmailController, email_model

api = Namespace('email', description='Operações de envio de e-mail')

email_request = api.model('EmailRequest', email_model)

@api.route('/send-email')
class SendEmail(Resource):
    @api.expect(email_request)
    @api.response(200, 'E-mail enviado com sucesso.')
    @api.response(500, 'Falha ao enviar e-mail.')
    def post(self):
        controller = EmailController(api)
        try:
            return controller.post()
        except Exception as e:
            api.abort(500, f'Falha ao enviar e-mail: {str(e)}')
