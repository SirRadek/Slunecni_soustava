import math

class Teleso:
    """
    Základní třída pro jakékoli nebeské těleso.
    Má atributy:
      - barva:   pro vykreslení (RGB tuple)
      - polomer: pro vykreslení (v pixelech)
    """
    def __init__(
        self,
        jmeno: str,
        hmotnost: float,
        polomer_drahy: float,
        uhlova_rychlost: float,
        pocatecni_uhel: float = 0.0,
        barva: tuple = (255, 255, 255),
        polomer: int = 5
    ):
        self.jmeno = jmeno
        self.hmotnost = hmotnost
        self.polomer_drahy = polomer_drahy
        self.uhlova_rychlost = uhlova_rychlost
        self.uhel = pocatecni_uhel

        # TYTO DVA ATRIBUTY potřebujeme pro vykreslení
        self.barva = barva
        self.polomer = polomer

        # počáteční souřadnice (relativně k barycentru)
        self.x = polomer_drahy * math.cos(self.uhel)
        self.y = polomer_drahy * math.sin(self.uhel)

    def update_pozice(self, dt: float):
        self.uhel += self.uhlova_rychlost * dt
        self.x = self.polomer_drahy * math.cos(self.uhel)
        self.y = self.polomer_drahy * math.sin(self.uhel)


class Planeta(Teleso):
    def __init__(
        self,
        jmeno: str,
        hmotnost: float,
        polomer_drahy: float,
        uhlova_rychlost: float,
        pocatecni_uhel: float = 0.0,
        barva: tuple = (0, 0, 255),
        polomer: int = 8
    ):
        super().__init__(
            jmeno,
            hmotnost,
            polomer_drahy,
            uhlova_rychlost,
            pocatecni_uhel,
            barva,
            polomer
        )


class Mesic(Teleso):
    def __init__(
        self,
        jmeno: str,
        hmotnost: float,
        okruh_planety: Planeta,
        polomer_drahy: float,
        uhlova_rychlost: float,
        pocatecni_uhel: float = 0.0,
        barva: tuple = (200, 200, 200),
        polomer: int = 4
    ):
        super().__init__(
            jmeno,
            hmotnost,
            polomer_drahy,
            uhlova_rychlost,
            pocatecni_uhel,
            barva,
            polomer
        )
        self.okruh_planety = okruh_planety

    def update_pozice(self, dt: float):
        # nejprve otočíme měsíc kolem jeho vlastní orbity
        self.uhel += self.uhlova_rychlost * dt
        rel_x = self.polomer_drahy * math.cos(self.uhel)
        rel_y = self.polomer_drahy * math.sin(self.uhel)
        # pak přičteme polohu mateřské planety
        self.x = self.okruh_planety.x + rel_x
        self.y = self.okruh_planety.y + rel_y
