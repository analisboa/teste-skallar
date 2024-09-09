import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import Config
import logging



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailService:
    def send_email(self, to, subject, body):
        msg = MIMEMultipart()
        msg['From'] = Config.EMAIL_HOST_USER
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            logger.info(f"Conectando ao servidor SMTP: {Config.EMAIL_HOST}:{Config.EMAIL_PORT}")
            server = smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT)
            if Config.EMAIL_USE_TLS:
                logger.info("Iniciando TLS")
                server.starttls()

            logger.info(f"R : {Config.EMAIL_HOST_USER}")
            server.login(Config.EMAIL_HOST_USER, Config.EMAIL_HOST_PASSWORD)

            logger.info("Enviando o e-mail")
            text = msg.as_string()
            server.sendmail(Config.EMAIL_HOST_USER, to, text)
            server.quit()

            logger.info(f"E-mail enviado com sucesso para: {to}")
            return {"message": "E-mail enviado com sucesso."}, 200
        
        except smtplib.SMTPAuthenticationError:
            logger.error("Falha na autenticação com o servidor SMTP.")
            return {"message": "Falha na autenticação com o servidor SMTP."}, 500
        
        except smtplib.SMTPConnectError:
            logger.error("Falha na conexão com o servidor SMTP.")
            return {"message": "Falha na conexão com o servidor SMTP."}, 500
        except smtplib.SMTPException as e:
            logger.error(f"Erro no envio do e-mail: {str(e)}")
            return {"message": f"Erro no envio do e-mail: {str(e)}"}, 500

        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")
            return {"message": f"Falha no envio do e-mail: {str(e)}"}, 500
