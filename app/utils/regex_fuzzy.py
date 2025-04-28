from fuzzywuzzy import process
from app.utils.normalize import normalizar_texto


def encontrar_palavra_chave(texto, lista_palavras_chave):
    """Usa fuzzy matching para encontrar a palavra-chave mais próxima do texto."""
    texto_normalizado = normalizar_texto(texto)
    melhor_correspondencia = process.extractOne(texto_normalizado, lista_palavras_chave)

    if melhor_correspondencia and melhor_correspondencia[1] > 60:
        return melhor_correspondencia[0]
    return None
