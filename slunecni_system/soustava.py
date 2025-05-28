import pygame
from slunecni_system.telesa import Teleso

class Soustava:
    def __init__(self, sirka=800, vyska=600):
        pygame.init()
        self.screen = pygame.display.set_mode((sirka, vyska))
        pygame.display.set_caption("Simulátor sluneční soustavy")
        self.clock = pygame.time.Clock()
        self.stred_x = sirka // 2
        self.stred_y = vyska // 2

        self.telesa: list[Teleso] = []
        self.bezi = True
        self.pauza = False

    def pridej_teleso(self, teleso: Teleso):
        self.telesa.append(teleso)

    def krok(self, dt):
        for t in self.telesa:
            t.update_pozice(dt)

    def vypocitej_barycentrum(self):
        total = sum(t.hmotnost for t in self.telesa)
        if total == 0:
            return 0, 0
        x = sum(t.hmotnost * t.x for t in self.telesa) / total
        y = sum(t.hmotnost * t.y for t in self.telesa) / total
        return x, y

    def vykresli(self):
        self.screen.fill((0, 0, 0))
        bary_x, bary_y = self.vypocitej_barycentrum()

        for t in self.telesa:
            # překlad relativně k barycentru
            sx = self.stred_x + int(t.x - bary_x)
            sy = self.stred_y + int(t.y - bary_y)
            pygame.draw.circle(self.screen, t.barva, (sx, sy), t.polomer)

        pygame.display.flip()

    def spust_pygame(self):
        while self.bezi:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.bezi = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_SPACE:
                        self.pauza = not self.pauza
                    elif ev.key == pygame.K_r:
                        for t in self.telesa:
                            t.uhel = 0
                            t.update_pozice(0)

            if not self.pauza:
                dt = self.clock.get_time() / 1000.0
                self.krok(dt)

            self.vykresli()
            self.clock.tick(60)

        pygame.quit()