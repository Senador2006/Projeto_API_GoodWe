import random
from app.utils.normalize import normalizar_texto
from app.utils.regex_fuzzy import encontrar_palavra_chave

# Banco de respostas expandido
respostas_variaveis = {
    ('status', 'inversor'): [
        "O inversor está funcionando perfeitamente.",
        "O status do inversor é normal."
    ],
    ('status', 'energia'): [
        "A energia está sendo distribuída corretamente.",
        "O fornecimento de energia está estável."
    ],
    ('produção', 'energia'): [
        "A produção de energia está em 5.2 kW.",
        "Atualmente estamos gerando 4.8 kW."
    ],
    ('geração', 'energia'): [
        "A geração de energia está ativa.",
        "Estamos gerando energia normalmente."
    ],
    ('ligar', 'bateria'): [
        "A bateria interna foi ativada.",
        "A bateria interna está ligada e operante."
    ],
    ('carregar', 'carro'): [
        "O carregamento do carro começou.",
        "Iniciei o carregamento do veículo híbrido."
    ]
}


class AlexaService:
    def processar_comando(self, comando):
        """Processa o comando separando intenção e entidade."""
        comando_normalizado = normalizar_texto(comando)

        intencoes = ['status', 'produção', 'geração', 'ligar', 'carregar']
        entidades = ['inversor', 'energia', 'bateria', 'carro']

        intencao_encontrada = encontrar_palavra_chave(comando_normalizado, intencoes)
        entidade_encontrada = encontrar_palavra_chave(comando_normalizado, entidades)

        if intencao_encontrada and entidade_encontrada:
            chave = (intencao_encontrada, entidade_encontrada)
            if chave in respostas_variaveis:
                resposta = random.choice(respostas_variaveis[chave])
                return {
                    "status": "OK",
                    "message": resposta
                }

        return {
            "status": "Error",
            "message": "Comando não compreendido ou dados insuficientes."
        }
