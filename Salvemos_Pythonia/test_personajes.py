import unittest
from personajes import Guerrero, Mago, Asesino

class TestPersonajes(unittest.TestCase):
    def test_guerrero_stats(self):
        g = Guerrero("Alex")
        self.assertEqual(g.vida, 120)
        self.assertEqual(g.ataque, 12)
        self.assertEqual(g.defensa, 8)
        self.assertEqual(g.tipo, "Guerrero")

    def test_mago_stats(self):
        m = Mago("Merlin")
        self.assertEqual(m.vida, 80)
        self.assertEqual(m.ataque, 18)
        self.assertEqual(m.defensa, 3)
        self.assertEqual(m.tipo, "Mago")

    def test_subir_nivel(self):
        a = Asesino("Ezio")
        nivel_inicial = a.nivel
        a.ganar_experiencia(120)  # Sube de nivel
        self.assertEqual(a.nivel, nivel_inicial + 1)
        self.assertLess(a.experiencia, 100)

if __name__ == "__main__":
    unittest.main()