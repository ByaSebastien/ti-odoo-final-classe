"""Monster : chaque espèce redéfinit ses statistiques en attributs de classe."""

import random
from collections.abc import Sequence
from typing import override

from final_classe.characters.base import Character
from final_classe.characters.hit import Hit


class Monster(Character):
    """Un monstre de Final Classe."""

    NAME = "Monstre"
    HP = 100
    MP = 0
    STRENGTH = 10
    MAGIC = 1
    DEFENSE = 1
    RESISTANCE = 1
    SPEED = 10
    XP = 0
    GIL = 0

    def __init__(self, name: str | None = None) -> None:
        super().__init__(
            name or self.NAME,
            self.HP,
            self.MP,
            self.STRENGTH,
            self.MAGIC,
            self.DEFENSE,
            self.RESISTANCE,
            self.SPEED,
        )
        self.xp = self.XP
        self.gil = self.GIL

    @property
    @override
    def title(self) -> str:
        """Un monstre n'a pas de job."""
        return "Monstre"

    def act(self, heroes: Sequence[Character]) -> list[Hit]:
        """Le tour du monstre : il attaque un héros debout, au hasard.

        Renvoie un Hit par coup porté.
        """
        target = random.choice([hero for hero in heroes if hero.is_alive])
        return [Hit("attaque", target, self.attack(target))]