"""Le catalogue : chaque fonction fabrique une pièce neuve."""

from final_classe.items.equipment import Equipment


def bronze_sword() -> Equipment:
    """Une épée simple."""
    return Equipment("Épée de bronze", "arme", 100, strength=4)


def rod() -> Equipment:
    """Le bâton des mages."""
    return Equipment("Bâton", "arme", 100, magic=4)


def leather_armor() -> Equipment:
    """Une armure légère."""
    return Equipment("Armure de cuir", "armure", 100, defense=4)


def chain_mail() -> Equipment:
    """Une armure plus lourde, qui protège aussi un peu de la magie."""
    return Equipment("Cotte de mailles", "armure", 300, defense=8, resistance=2)