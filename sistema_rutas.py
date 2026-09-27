# ==========================================
# SISTEMA INTELIGENTE DE RUTAS
# ==========================================

# ==========================================
# 1. BASE DE CONOCIMIENTO
# ==========================================

# Este diccionario representa el grafo (mapa) de nuestro sistema de transporte.
# Las "llaves" son las estaciones y los "valores" son listas con las estaciones vecinas.
rutas = {
    "Portal Norte": ["Calle 100"],
    "Calle 100": ["Portal Norte", "Héroes"],
    "Héroes": ["Calle 100", "Calle 72"],
    "Calle 72": ["Héroes", "Calle 63", "Museo Nacional"],
    "Calle 63": ["Calle 72", "Calle 57", "Centro"],
    "Calle 57": ["Calle 63", "Calle 45"],
    "Calle 45": ["Calle 57", "Marly"],
    "Marly": ["Calle 45", "Museo Nacional"],
    "Museo Nacional": ["Marly", "Centro"],
    "Centro": ["Museo Nacional", "Avenida El Dorado"],
    "Avenida El Dorado": ["Centro"]
}


# ==========================================
# 2. CÓDIGOS DE LAS ESTACIONES
# ==========================================

# Diccionario auxiliar para mejorar la experiencia del usuario. 
# Permite ingresar una sola letra en lugar de escribir todo el nombre (evita errores de tipeo).
estaciones = {
    "A": "Portal Norte",
    "B": "Calle 100",
    "C": "Héroes",
    "D": "Calle 72",
    "E": "Calle 63",
    "F": "Calle 57",
    "G": "Calle 45",
    "H": "Marly",
    "I": "Museo Nacional",
    "J": "Centro",
    "K": "Avenida El Dorado"
}


# ==========================================
# 3. BUSCAR RUTA
# ==========================================

def buscar_ruta(origen, destino, ruta=[]):

    # Agregamos la estación actual a la lista de la ruta que estamos trazando
    ruta = ruta + [origen]

    # Si llegamos a nuestro destino, devolvemos la ruta completa
    if origen == destino:
        return ruta

    # Exploramos una por una las estaciones conectadas a nuestra estación actual
    for estacion in rutas[origen]:

        # Verificamos que la estación no esté ya en la ruta para evitar dar vueltas en círculos
        if estacion not in ruta:

            # Llamamos a la función nuevamente (recursividad) para avanzar a la siguiente estación
            nueva_ruta = buscar_ruta(
                estacion,
                destino,
                ruta
            )

            # Si esta exploración encontró un camino válido hacia el destino, lo retornamos
            if nueva_ruta:
                return nueva_ruta

    # Si revisamos todas las opciones posibles y no hay salida, devolvemos None
    return None


# ==========================================
# 4. PROGRAMA PRINCIPAL
# ==========================================

# Interfaz de texto que se mostrará en la consola al iniciar el programa
print("========================================")
print("      SISTEMA INTELIGENTE DE RUTAS")
print("========================================")

print("\nEstaciones disponibles:")

# Recorremos el diccionario de estaciones para imprimir el menú de opciones (Ej: "A. Portal Norte")
for letra, nombre in estaciones.items():
    print(f"{letra}. {nombre}")


# ==========================================
# 5. INGRESAR ORIGEN Y DESTINO
# ==========================================

# Solicitamos al usuario que ingrese las letras. 
# El método .upper() convierte automáticamente la entrada a mayúscula por si el usuario usa minúsculas.
origen_letra = input("\nIngrese la letra de la estación de origen: ").upper()
destino_letra = input("Ingrese la letra de la estación de destino: ").upper()


# ==========================================
# 6. VALIDAR
# ==========================================

# Validamos que la letra de origen ingresada exista en nuestro diccionario de estaciones
if origen_letra not in estaciones:

    print("\nLa estación de origen no existe.")

# Validamos que la letra de destino ingresada exista en nuestro diccionario de estaciones
elif destino_letra not in estaciones:

    print("\nLa estación de destino no existe.")

# Si ambas letras son correctas (existen en el diccionario), procedemos a buscar la ruta
else:

    # Convertimos las letras ingresadas a los nombres reales de las estaciones
    origen = estaciones[origen_letra]
    destino = estaciones[destino_letra]

    # Ejecutamos nuestra función recursiva para encontrar el camino
    resultado = buscar_ruta(origen, destino)

    # Si la función nos devuelve una ruta válida (la variable contiene datos)
    if resultado:

        print("\n========================================")
        print("          MEJOR RUTA ENCONTRADA")
        print("========================================")

        # Imprimimos la lista de estaciones separadas por una flecha " -> " en una sola línea
        print(" -> ".join(resultado))

        # Contamos cuántas estaciones tiene la lista para dar el total del recorrido
        print("\nNúmero de estaciones:", len(resultado))

    # Si la función devuelve None, significa que no hay conexión posible en el mapa
    else:

        print("\nNo existe una ruta entre las estaciones.")