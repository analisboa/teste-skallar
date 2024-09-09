import pytest
from unittest.mock import patch
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.controladores.email_controlador.EmailController.post')
def test_send_email_success(mock_post, client):
    mock_post.return_value = {"message": "E-mail enviado com sucesso."}, 200

    payload = {
        "to": "testesana19@gmail.com",
        "subject": "Teste de envio de E-mail com sucesso",
        "body": "Este é um e-mail de teste para processo seletivo da Skallar."
    }

    response = client.post('/api/send-email', json=payload)
    assert response.status_code == 200
    assert response.get_json()['message'] == "E-mail enviado com sucesso."

@patch('app.controladores.email_controlador.EmailController.post')
def test_send_email_failure(mock_post, client):
    mock_post.side_effect = Exception("Erro de envio.")

    payload = {
        "to": "testesana19@gmail.com",
        "subject": "Teste de envio de falha no envio de E-mail",
        "body": "Este é um e-mail de teste na situação de falha."
    }
    
    response = client.post('/api/send-email', json=payload)
    assert response.status_code == 500
    assert "Falha ao enviar e-mail" in response.get_json()['message']
