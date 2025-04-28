from app.models.goodwe_model import GoodWeData

class GoodWeService:
    def obter_status_inversor(self):
        # Aqui você pode pegar os dados reais da API da GoodWe
        # Para a demonstração, vamos criar um objeto GoodWeData com valores simulados
        dados = GoodWeData(status="Ativo", production=5.2, battery_level=75)
        return dados.to_dict()

    def obter_producao_energia(self):
        # Simulando o retorno de dados de produção de energia
        dados = GoodWeData(status="Ativo", production=5.2, battery_level=75)
        return dados.to_dict()
