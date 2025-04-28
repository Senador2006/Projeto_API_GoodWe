import unittest
from app.services.alexa_service import AlexaService

class TestAlexaService(unittest.TestCase):
    def setUp(self):
        self.alexa_service = AlexaService()

    def test_processar_comando_status(self):
        comando = "Qual é o status do inversor?"
        resposta = self.alexa_service.processar_comando(comando)
        self.assertEqual(resposta['status'], 'OK')
        self.assertIn(resposta['message'], [
            "O status do inversor está funcionando perfeitamente.",
            "O inversor está operando normalmente.",
            "Tudo está bem com o inversor.",
            "O inversor está em funcionamento."
        ])

    def test_processar_comando_producao(self):
        comando = "Qual a produção de energia?"
        resposta = self.alexa_service.processar_comando(comando)
        self.assertEqual(resposta['status'], 'OK')
        self.assertIn(resposta['message'], [
            "A produção de energia está em 5.2 kW.",
            "Estamos gerando 4.8 kW de energia.",
            "A produção de energia é 5.5 kW.",
            "Geramos 5.0 kW de energia atualmente."
        ])

    def test_processar_comando_geracao(self):
        comando = "Qual a geração de energia?"
        resposta = self.alexa_service.processar_comando(comando)
        self.assertEqual(resposta['status'], 'OK')
        self.assertIn(resposta['message'], [
            "A geração de energia está ativa.",
            "A geração está fluindo como esperado.",
            "A geração de energia está em pleno funcionamento.",
            "Estamos gerando energia de maneira eficiente."
        ])

    def test_processar_comando_invalido(self):
        comando = "Qual o tempo vai fazer hoje?"
        resposta = self.alexa_service.processar_comando(comando)
        self.assertEqual(resposta['status'], 'Error')
        self.assertEqual(resposta['message'], "Comando não reconhecido.")

if __name__ == '__main__':
    unittest.main()
