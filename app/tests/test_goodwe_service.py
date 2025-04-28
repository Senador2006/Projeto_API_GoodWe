import unittest
from app.services.goodwe_service import GoodWeService

class TestGoodWeService(unittest.TestCase):
    def setUp(self):
        self.goodwe_service = GoodWeService()

    def test_obter_status_inversor(self):
        status = self.goodwe_service.obter_status_inversor()
        self.assertEqual(status['status'], 'Ativo')
        self.assertEqual(status['production'], 5.2)
