class Jugador:
    def __init__(self, nombre, vida, ataque, defensa, velocidad, nivel=1, experiencia=0, tipo="Guerrero"):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.nivel = nivel
        self.experiencia = experiencia
        self.tipo = tipo

    def mostrar_stats(self):
        print(f"\n--- {self.nombre} ({self.tipo}) ---")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Experiencia: {self.experiencia}/100\n")

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        print(f"\nHas ganado {cantidad} XP.")

        while self.experiencia >= 100:
            self.experiencia -= 100
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 20
        self.ataque += 5
        self.defensa += 3
        print(f"\n🎉 ¡Has subido al nivel {self.nivel}!")
        print("Tus estadísticas han mejorado.")
        self.mostrar_stats()

# Clases derivadas con stats iniciales diferentes
class Guerrero(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre, vida=120, ataque=12, defensa=8, velocidad=7, tipo="Guerrero")

class Mago(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=18, defensa=3, velocidad=10, tipo="Mago")

class Asesino(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque=14, defensa=4, velocidad=12, tipo="Asesino")

class Clerigo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre, vida=100, ataque=10, defensa=6, velocidad=8, tipo="Clérigo")
