# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    pali = texto.replace(" ", "").lower()
    while len(pali) > 1:
            if pali[0] != pali[-1]:
                return False
            pali = pali[1:-1]   
    return True 
    pass


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    texto = texto.title()
    return texto
    pass


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador
    pass


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            codigo_base = ord('A') if letra.isupper() else ord('a')
            letra_cifrada = chr((ord(letra) - codigo_base + desplazamiento) % 26 + codigo_base)
            resultado += letra_cifrada
        else:
            resultado += letra
    return resultado
    pass
