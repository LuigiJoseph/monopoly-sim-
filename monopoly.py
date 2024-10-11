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
# practice_with_dice()



def throw_two_dice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    result = dice_1 + dice_2
    
    return result

def simulate_monopoly_games(total_games: int): 
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400] #A value of 0 means, the field is empty (not for sale)

    current_position = 0

    for throw in range(100):
        if throw == 0:
            current_position = 0
        num_throw = 0
        if board_values[current_position] == 0:
            print(f"throw {num_throw} position: {board_values[current_position]} (empty)")
        if board_values[current_position] != 0:
            print(f"throw {num_throw} position: {board_values[current_position]} (property)")
        num_throw += 1
        current_position = throw_two_dice() + current_position

        #Wrap around the board using modulus to prevent index out of range
        current_position %= len(board_values)

simulate_monopoly_games(1)

def main():
    pass
