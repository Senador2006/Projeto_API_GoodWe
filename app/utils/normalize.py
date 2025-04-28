import unicodedata
import re

def normalizar_texto(texto):
    """Normaliza texto removendo acentuação, pontuação e deixando minúsculo."""
    texto_normalizado = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto_normalizado = re.sub(r'[^\w\s]', '', texto_normalizado)
    texto_normalizado = texto_normalizado.lower()
    return texto_normalizado
