"""Le bestiaire : une classe par espèce."""

from final_classe.characters.monster import Monster


class Flan(Monster):
    """Sa gélatine encaisse les coups, mais craint la magie."""

    NAME = "Flan"
    HP = 450
    STRENGTH = 14
    DEFENSE = 18
    RESISTANCE = 4
    SPEED = 6
    XP = 60
    GIL = 50


class Wolf(Monster):
    """Il mord fort et vite, mais se protège mal."""

    NAME = "Loup"
    HP = 380
    STRENGTH = 16
    DEFENSE = 6
    RESISTANCE = 8
    SPEED = 14
    XP = 80
    GIL = 60


class Sephiroth(Monster):
    """Le souvenir de Nibelheim. Pour l'instant, hors d'atteinte."""

    NAME = "Sephiroth"
    HP = 30000
    MP = 999
    STRENGTH = 50
    MAGIC = 60
    DEFENSE = 99
    RESISTANCE = 99
    SPEED = 30