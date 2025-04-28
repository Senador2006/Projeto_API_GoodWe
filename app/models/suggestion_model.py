class Suggestion:
    def __init__(self, tipo, mensagem):
        self.tipo = tipo
        self.mensagem = mensagem

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "mensagem": self.mensagem
        }
