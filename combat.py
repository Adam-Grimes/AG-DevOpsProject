# Define a function 'calculate_damage' that takes two integers, 'attack' and 'defense'
# It is type-hinted to return an integer
def calculate_damage(attack: int, defense: int) -> int:
    """
    Calculates damage dealt, ensuring a minimum of 1 damage is always returned
    to prevent ties from halting combat progression.
    """
    
    # Calculate the raw damage by subtracting defense from attack
    damage = attack - defense
    
    # Check if the calculated damage is less than 1
    if damage < 1:
        # If damage is 0 or negative, return 1 to ensure minimum damage
        return 1
    
    # If damage is 1 or more, return the calculated damage
    return damage