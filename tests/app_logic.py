# app_logic.py

def validar_senha(senha):
    """
    Valida a força da senha baseado em 3 regras:
    1. Pelo menos 8 caracteres.
    2. Pelo menos um número.
    3. Pelo menos uma letra maiúscula.
    """
    if not senha:
        return False

    tem_min_8_caracteres = len(senha) >= 8
    tem_numero = any(char.isdigit() for char in senha)
    tem_maiuscula = any(char.isupper() for char in senha)

    # Retorna True APENAS se todas as regras forem verdadeiras
    return tem_min_8_caracteres and tem_numero and tem_maiuscula