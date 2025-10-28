def calculate_damage(attack: int, defense: int) -> int:
    """
    Calculates damage dealt, ensuring a minimum of 1 damage is always returned
    to prevent ties from halting combat progression.
    """
    damage = attack - defense
    
    if damage < 1:
        return 1
    
    return damage