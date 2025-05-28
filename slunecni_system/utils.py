import math

# Gravitační konstanta (m^3 kg^-1 s^-2)
G = 6.67430e-11


def deg_to_rad(degrees: float) -> float:
    """
    Převod úhlů z stupňů na radiány.
    """
    return degrees * math.pi / 180.0


def rad_to_deg(radians: float) -> float:
    """
    Převod úhlů z radiánů na stupně.
    """
    return radians * 180.0 / math.pi


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Vzdálenost dvou bodů v rovině.
    """
    return math.hypot(x2 - x1, y2 - y1)


def gravitational_force(m1: float, m2: float, r: float) -> float:
    """
    Výpočet velikosti gravitační síly mezi dvěma hmotami.
    F = G * m1 * m2 / r^2
    Vrací 0, pokud r == 0.
    """
    if r == 0:
        return 0.0
    return G * m1 * m2 / (r ** 2)


def gravitational_acceleration(mass: float, r: float) -> float:
    """
    Gravitační zrychlení v dané vzdálenosti od hmotného bodu.
    a = G * mass / r^2
    Vrací 0, pokud r == 0.
    """
    if r == 0:
        return 0.0
    return G * mass / (r ** 2)


def orbital_period(central_mass: float, radius: float) -> float:
    """
    Výpočet doby oběhu (perioda) tělesa na kruhové dráze kolem centrální hmoty.
    T = 2 * pi * sqrt(r^3 / (G * M))
    """
    return 2 * math.pi * math.sqrt((radius ** 3) / (G * central_mass))


def clamp(value: float, minimum: float, maximum: float) -> float:
    """
    Omezí hodnotu na daný interval [minimum, maximum].
    """
    return max(minimum, min(maximum, value))
