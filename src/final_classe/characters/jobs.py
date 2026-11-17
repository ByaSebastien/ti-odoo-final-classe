"""Les jobs : chaque classe redéfinit des attributs de classe, et écrit sa compétence."""

from typing import override

from final_classe.characters.base import Character
from final_classe.characters.hero import Hero


class Soldier(Hero):
    """Le Soldat : une épée immense, et Omnislash."""

    BASE_HP = 700
    BASE_MP = 50
    SPEED = 12
    JOB_NAME = "Soldat"
    SKILL_NAME = "Omnislash"
    SKILL_COST = 12

    @override
    def skill_effect(self, target: Character) -> int:
        """Trois coups d'épée d'affilée."""
        return sum(self.attack(target) for _ in range(3))


class BlackMage(Hero):
    """Le Mage noir : fragile, mais Feu fait mal."""

    BASE_HP = 520
    BASE_MP = 90
    SPEED = 10
    JOB_NAME = "Mage noir"
    SKILL_NAME = "Feu"
    SKILL_COST = 8
    SKILL_TEXT = "{user} lance Feu sur {target} : {value} dégâts."

    @override
    def skill_effect(self, target: Character) -> int:
        """Une attaque magique."""
        return self.magic_attack(target, 12)