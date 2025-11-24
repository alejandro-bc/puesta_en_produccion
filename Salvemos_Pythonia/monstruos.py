from db import get_connection

class Monstruo:
    def __init__(self, nombre, vida, ataque, defensa, experiencia):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.experiencia = experiencia

def generar_monstruo():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, vida, ataque, defensa, experiencia FROM monstruos ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()

    if row:
        nombre, vida, ataque, defensa, experiencia = row
        return Monstruo(nombre, vida, ataque, defensa, experiencia)
    else:
        return None
