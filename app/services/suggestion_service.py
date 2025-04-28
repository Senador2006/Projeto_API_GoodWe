from app.utils.suggestions import Suggestions

class SuggestionService:
    def __init__(self):
        self.sugestoes = Suggestions()

    def obter_sugestao_clima(self):
        return self.sugestoes.obter_sugestao_clima()
