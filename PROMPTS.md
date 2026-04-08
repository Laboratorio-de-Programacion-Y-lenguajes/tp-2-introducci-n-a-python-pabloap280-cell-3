# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: 


**Prompt usado**:
> 
*Podrias realizar el un commit detallando de este codigo (El codigo de la parte de variables)*


*match valor:

        case int():

            return "int"

        case str():

            return "str"

        case float():

            return "float"

        case bool():

            return "bool"

    pass

por que me tira error en este codigo?*

**Resultado obtenido**:

**feat: agregar utilidades de saludo y validación de tipos

- Añadida función `crear_saludo` para strings formateados.
- Añadida `suma_enteros` y `convertir_a_float` para operaciones básicas.
- Implementada `es_mayor_de_edad` con retorno booleano directo.
- Implementada `tipo_de_dato` usando pattern matching optimizado para bool e int.**

**def identificar_tipo(valor):
    match valor:
        case bool(): # El booleano debe ir primero
            return "bool"
        case int():
            return "int"
        case str():
            return "str"
        case float():
            return "float"
        case _:
            return "desconocido"**
**¿Lo usaste tal cual o lo modificaste?**


---

### 2 - condicionales.py

**Herramienta**: 

**Prompt usado**:
> 

*Podrias realizar el un commit detallando de este codigo (El codigo de la parte de condicionales)*

**Resultado obtenido**:



**¿Lo usaste tal cual o lo modificaste?**

**feat: implementar funciones de lógica condicional y clasificación

- Añadida `clasificar_numero` para determinar el signo de un entero.
- Añadida `mayor_de_tres` para encontrar el valor máximo entre tres números.
- Añadida `clasificar_nota` para categorizar calificaciones académicas.
- Añadida `es_bisiesto` con la lógica de validación de años según el calendario gregoriano.**
---

### 3 - listas.py

**Herramienta**: 

**Prompt usado**:
> 
*Podrias realizar el un commit detallando de este codigo (El codigo de la parte de listas)*

*"""

    Retorna una nueva lista sin elementos duplicados,

    manteniendo el orden de primera aparición.

    """ como resolver esta peticion*

**Resultado obtenido**:

**feat: agregar funciones para manipulación y filtrado de listas

- Añadida `suma_lista` para agregación de elementos.
- Añadida `filtrar_pares` para selección condicional.
- Añadida `invertir_lista` mediante slicing (sin mutar la original).
- Implementada `eliminar_duplicados` preservando el orden de aparición.
- Implementada `aplanar_lista` para procesar listas anidadas de un nivel.**

**sin_duplicados = []
    for elemento in lista:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    return sin_duplicados**

**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

*Podrias realizar el un commit detallando de este codigo (El codigo de la parte de diccionarios)*


*"""

    Retorna un diccionario con la frecuencia de cada palabra.

    Ejemplo: contar_palabras("hola mundo hola") -> {"hola": 2, "mundo": 1}

    Las palabras deben ser comparadas en minúsculas.

    """ como resolver esta peticion*
    

**Resultado obtenido**:

**feat: agregar utilidades para el manejo y filtrado de diccionarios

- Implementada `contar_palabras` para análisis de frecuencia de términos.
- Añadida `invertir_diccionario` para intercambio de pares clave-valor.
- Añadida `merge_diccionarios` con lógica de actualización (prevalece d2).
- Añadida `filtrar_por_valor` para selección condicional de datos.**

**frecuencia = {}
    for palabra in texto.split():
        palabra = palabra.lower()
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
    pass**

**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

*Podrias realizar el un commit detallando de este codigo (El codigo de la parte de loops)*

*"""
    Retorna True si n es un número primo.
    """ como resolver esta peticion*

*"""

    Retorna los primeros n números de la serie de Fibonacci.

    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]

    """ como resolver esta peticion*

**Resultado obtenido**:

**feat: implementar funciones de secuencias numéricas y lógica matemática

- Añadida `contar_hasta` y `tabla_multiplicar` mediante generadores de listas.
- Añadida `suma_digitos` usando conversión a strings y acumulación.
- Implementada `es_primo` con optimización de raíz cuadrada ($n^{0.5}$).
- Implementada `fibonacci` para generar la serie hasta el n-ésimo término.**

**if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True**

**def fibonacci(n: int) -> list[int]:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Si n <= 0, retorna una lista vacía.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    serie = [0, 1]
    while len(serie) < n:
        # Sumamos los dos últimos elementos para obtener el siguiente
        siguiente = serie[-1] + serie[-2]
        serie.append(siguiente)
        
    return serie**
**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

*Podrias realizar el un commit detallando de este codigo (El codigo de la parte de funciones)*

*"""

    Retorna una versión de func que cachea sus resultados.

    Si se llama con los mismos argumentos, retorna el resultado cacheado.

    """ como resolver esta peticion*

**Resultado obtenido**:

**feat: implementar funciones de orden superior y optimización

- Añadida `aplicar_funcion` como implementación personalizada de map.
- Añadida `componer` para la creación de tuberías de funciones ($f \circ g$).
- Implementado el decorador `memoizar` para cache de resultados y mejora de rendimiento.
- Añadida `reducir` para procesos de acumulación sin dependencias externas.**

**cache = {}

    def memoizada(*args):
        # Si los argumentos ya están en el cache, retornamos el valor guardado
        if args in cache:
            return cache[args]
        
        # Si no, calculamos el resultado y lo guardamos
        resultado = func(*args)
        cache[args] = resultado
        return resultado

    return memoizada**

**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

*Podrias realizar el un commit detallando de este codigo (El codigo de la parte de coperaciones)*

*"""

    Aplica el cifrado César al texto con el desplazamiento dado.

    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.

    Ejemplo: caesar_cipher("abc", 1) -> "bcd"

    """ como resolver esta peticion*

**Resultado obtenido**:

**feat: implementar utilidades de manipulación y cifrado de texto

- Añadida `es_palindromo` con lógica recursiva de strings e ignorancia de espacios/mayúsculas.
- Añadida `capitalizar_palabras` utilizando el método title().
- Añadida `contar_vocales` con soporte para mayúsculas y minúsculas.
- Implementado `caesar_cipher` para cifrado por desplazamiento manteniendo tipos de caracteres.**

**def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    """
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Determinar si es mayúscula o minúscula para establecer la base ASCII
            base = ord('A') if char.isupper() else ord('a')
            # Aplicar desplazamiento con operador módulo para que vuelva a empezar de la 'a'
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nuevo_char
        else:
            # Mantener caracteres especiales, espacios o números intactos
            resultado += char
    return resultado**

**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
