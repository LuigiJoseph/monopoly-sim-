import random


def practice_with_dice():
    total_doubles = 0

    for i in range(1000):
        # Simulate two dice rolls
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        
        # Print the total value of the dice
        print(f"Throw {i+1}: Dice 1 = {dice1}, Dice 2 = {dice2}, Total = {total}")
        
        # Check if a double was thrown
        if dice1 == dice2:
            print("** Double! **")
            total_doubles += 1
    
    # Print the total number of doubles at the end
    print(f"\nTotal number of doubles thrown: {total_doubles}")

# Testing the function
practice_with_dice()



def throw_two_dice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    result = dice_1 + dice_2
    
    return result

def simulate_monopoly_games(total_games: int) -> int: 
    pass

def main():
    pass
