def calculate_damage(attack: int, defense: int) -> int:
    """
    Calculates damage dealt, ensuring a minimum of 1 damage is always returned
    to prevent ties from halting combat progression.

    Args:
        attack: The offensive power statistic of the attacker.
        defense: The defensive power statistic of the defender.

    Returns:
        The total damage dealt (minimum 1).
    """
    
    # 1. Standard damage calculation: Attack minus Defense.
    damage = attack - defense
    
    # 2. Minimum Damage Rule (The Core Game Logic)
    # Checks if the result is zero or negative.
    if damage < 1:
        # If defense cancels out or exceeds attack, damage is capped at 1.
        # This prevents combat from becoming stuck due to 0-damage exchanges.
        return 1
    
    # 3. Return calculated damage if it is greater than 1.
    return damage