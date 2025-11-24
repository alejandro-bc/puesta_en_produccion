import sqlite3
from personajes import Guerrero, Mago, Asesino, Clerigo

DB_NAME = "juego.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabla jugadores con la columna tipo
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jugador (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        tipo TEXT,
        vida INTEGER,
        ataque INTEGER,
        defensa INTEGER,
        nivel INTEGER,
        experiencia INTEGER
    )
    """)

    # Tabla monstruos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS monstruos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        vida INTEGER,
        ataque INTEGER,
        defensa INTEGER,
        experiencia INTEGER
    )
    """)

    # Tabla partidas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS partida (
        jugador_nombre TEXT,
        personaje_nombre TEXT,
        tipo TEXT,
        vida INTEGER,
        ataque INTEGER,
        defensa INTEGER,
        velocidad INTEGER,
        nivel INTEGER,
        experiencia INTEGER
    )
    """)

    # Insertar monstruos iniciales si no existen
    cursor.execute("SELECT COUNT(*) FROM monstruos")
    if cursor.fetchone()[0] == 0:
        iniciales = [
            ("Goblin", 40, 6, 2, 40),
            ("Orco", 60, 10, 5, 60),
            ("Troll", 80, 12, 6, 80)
        ]
        cursor.executemany(
            "INSERT INTO monstruos (nombre, vida, ataque, defensa, experiencia) VALUES (?, ?, ?, ?, ?)",
            iniciales
        )

    conn.commit()
    conn.close()

def guardar_jugador(jugador):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM jugador")  # Solo un jugador a la vez
    cursor.execute("""
    INSERT INTO jugador (nombre, tipo, vida, ataque, defensa, nivel, experiencia)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (jugador.nombre, jugador.tipo, jugador.vida, jugador.ataque,
          jugador.defensa, jugador.nivel, jugador.experiencia))

    conn.commit()
    conn.close()

def cargar_jugador():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT nombre, tipo, vida, ataque, defensa, nivel, experiencia
    FROM jugador LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()

    if row:
        nombre, tipo, vida, ataque, defensa, nivel, experiencia = row
        # Mapear tipo a clase
        clase_map = {
            "Guerrero": Guerrero,
            "Mago": Mago,
            "Asesino": Asesino,
            "Clerigo": Clerigo
        }
        jugador = clase_map[tipo](nombre)
        jugador.vida = vida
        jugador.ataque = ataque
        jugador.defensa = defensa
        jugador.nivel = nivel
        jugador.experiencia = experiencia
        return jugador
    return None

def guardar_personajes(personajes):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jugador")  # Borra todos los jugadores
    for jugador in personajes:
        cursor.execute("""
        INSERT INTO jugador (nombre, tipo, vida, ataque, defensa, nivel, experiencia)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (jugador.nombre, jugador.tipo, jugador.vida, jugador.ataque,
              jugador.defensa, jugador.nivel, jugador.experiencia))
    conn.commit()
    conn.close()

def cargar_personajes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT nombre, tipo, vida, ataque, defensa, nivel, experiencia
    FROM jugador
    """)
    rows = cursor.fetchall()
    conn.close()
    personajes = []
    clase_map = {
        "Guerrero": Guerrero,
        "Mago": Mago,
        "Asesino": Asesino,
        "Clerigo": Clerigo,
        "Clérigo": Clerigo
    }
    for row in rows:
        nombre, tipo, vida, ataque, defensa, nivel, experiencia = row
        tipo = tipo if tipo in clase_map else "Guerrero"
        jugador = clase_map[tipo](nombre)
        jugador.vida = vida
        jugador.ataque = ataque
        jugador.defensa = defensa
        jugador.nivel = nivel
        jugador.experiencia = experiencia
        jugador.tipo = tipo
        personajes.append(jugador)
    return personajes

def obtener_monstruo_aleatorio():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, vida, ataque, defensa, experiencia FROM monstruos ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        from monstruos import Monstruo
        return Monstruo(*row)
    return None

def guardar_partida(jugador_nombre, personajes):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM partida WHERE jugador_nombre = ?", (jugador_nombre,))
    for pj in personajes:
        cursor.execute("""
        INSERT INTO partida (jugador_nombre, personaje_nombre, tipo, vida, ataque, defensa, velocidad, nivel, experiencia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (jugador_nombre, pj.nombre, pj.tipo, pj.vida, pj.ataque, pj.defensa, pj.velocidad, pj.nivel, pj.experiencia))
    conn.commit()
    conn.close()

def cargar_partida(jugador_nombre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT personaje_nombre, tipo, vida, ataque, defensa, velocidad, nivel, experiencia
    FROM partida WHERE jugador_nombre = ?
    """, (jugador_nombre,))
    rows = cursor.fetchall()
    conn.close()
    personajes = []
    clase_map = {
        "Guerrero": Guerrero,
        "Mago": Mago,
        "Asesino": Asesino,
        "Clerigo": Clerigo,
        "Clérigo": Clerigo
    }
    for row in rows:
        nombre, tipo, vida, ataque, defensa, velocidad, nivel, experiencia = row
        tipo = tipo if tipo in clase_map else "Guerrero"
        pj = clase_map[tipo](nombre)
        pj.vida = vida
        pj.ataque = ataque
        pj.defensa = defensa
        pj.velocidad = velocidad
        pj.nivel = nivel
        pj.experiencia = experiencia
        pj.tipo = tipo
        personajes.append(pj)
    return personajes

def listar_jugadores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT jugador_nombre FROM partida")
    jugadores = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jugadores
