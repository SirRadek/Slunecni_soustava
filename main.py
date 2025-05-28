from slunecni_system.soustava import Soustava
from slunecni_system.telesa import Planeta, Mesic
from slunecni_system.utils import deg_to_rad

# — měřítko oběžných drah: 1 px = ORBIT_DIV milionů km
ORBIT_DIV = 7.0

# — měřítko poloměru těles: 1 px = RADIUS_SCALE km
RADIUS_SCALE = 0.001

# — skutečné poloměry v km
REAL_RADII = {
    "Slunce": 696_340,
    "Merkur": 2_440,
    "Venuse": 6_052,
    "Zeme":   6_371,
    "Mars":   3_390,
    "Jupiter":69_911,
    "Saturn": 58_232,
    "Uran":   25_362,
    "Neptun": 24_622,
    "Mesic":  1_737,
    "Phobos":    11,
    "Deimos":     6,
}

def main():
    # 1) Inicializace simulace
    sirka, vyska = 1600, 1200
    sys = Soustava(sirka=sirka, vyska=vyska)

    # 2) Seznam těl: (jméno, hmotnost [10^24 kg], dráha [mil. km], úhlová rychlost [rad/s], startovní uhel [°])
    planety = [
        ("Slunce", 1989_000,   0,      0,    0),
        ("Merkur",     0.330,  58,   4.15,    0),
        ("Venuse",     4.867, 108,   1.62,   45),
        ("Zeme",       5.972, 150,   1.00,   90),
        ("Mars",       0.641, 228,   0.53,  135),
        ("Jupiter",  1898.000,778,  0.084,  180),
        ("Saturn",    568.000,1427, 0.034,  225),
        ("Uran",       86.800,2871, 0.0119, 270),
        ("Neptun",   102.000,4495, 0.0055, 315),
    ]

    # 3) Vytvoření a přidání planet (s realitou poloměru a škálou drah)
    for jmeno, hmotnost, drha, rychlost, uhel_deg in planety:
        # drha v px
        drha_px = drha / ORBIT_DIV
        # polomer v px
        polom_px = max(1, int(REAL_RADII[jmeno] * RADIUS_SCALE))
        planeta = Planeta(
            jmeno=jmeno,
            hmotnost=hmotnost,
            polomer_drahy=drha_px,
            uhlova_rychlost=rychlost,
            pocatecni_uhel=deg_to_rad(uhel_deg),
            barva=(255,200,0) if jmeno=="Slunce" else None,  # Slunce žluté, ostatní mají default z telesa.py
            polomer=polom_px
        )
        sys.pridej_teleso(planeta)

        # 4) Přidání měsíců
        if jmeno == "Zeme":
            # Měsíc Země
            drha_m = 0.384  # 384 tisíc km = 0.384 mil. km
            drha_m_px = drha_m / ORBIT_DIV
            polom_m_px = max(1, int(REAL_RADII["Mesic"] * RADIUS_SCALE))
            moon = Mesic(
                "Mesic", 0.073,
                planeta,
                drha_m_px,
                rychlost*12,  # zrychleně pro lepší efekt
                deg_to_rad(0),
                barva=(200,200,200),
                polomer=polom_m_px
            )
            sys.pridej_teleso(moon)

        if jmeno == "Mars":
            # Phobos
            ph_r_px = max(1, int(REAL_RADII["Phobos"] * RADIUS_SCALE))
            ph_drha_px = 0.009 / ORBIT_DIV  # 9 tisíc km = 0.009 mil. km
            sys.pridej_teleso(Mesic("Phobos", 0.00001, planeta, ph_drha_px, rychlost*20, deg_to_rad(0), polomer=ph_r_px))
            # Deimos
            de_r_px = max(1, int(REAL_RADII["Deimos"] * RADIUS_SCALE))
            de_drha_px = 0.023 / ORBIT_DIV  # 23 tisíc km
            sys.pridej_teleso(Mesic("Deimos",0.000002,planeta,de_drha_px,rychlost*10,deg_to_rad(180),polomer=de_r_px))

    # 5) Spuštění Pygame smyčky
    sys.spust_pygame()

if __name__ == "__main__":
    main()
