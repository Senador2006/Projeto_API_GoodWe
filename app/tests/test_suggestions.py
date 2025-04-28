import unittest
from app.services.suggestion_service import SuggestionService

class TestSuggestionService(unittest.TestCase):
    def setUp(self):
        self.suggestion_service = SuggestionService()

    def test_obter_sugestao_clima(self):
        sugestao = self.suggestion_service.obter_sugestao_clima()
        self.assertIn(sugestao, [
            "Hoje haverá chuva forte, deseja armazenar a energia da bateria interna?",
            "O tempo está ensolarado, quer maximizar a produção de energia?",
            "Vai chover, deseja ajustar a carga da bateria?"
        ])
