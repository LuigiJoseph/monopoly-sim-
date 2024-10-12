import random
import matplotlib.pyplot as plt
from statistics import mean

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

def simulate_monopoly(starting_money): 
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400] #A value of 0 means, the field is empty (not for sale)

    possesions = [0] * 40
    
    current_position = 0
    current_money = starting_money
    num_of_buying = 0
    num_of_throw = 0
    num_of_properties = 28 #remaining properties
    

    while sum(board_values) != 0:

        # if board_values[current_position] == 0:
        #     print(f"throw {num_of_throw} position: {current_position} (empty)") #cant buy (is empty)

        if board_values[current_position] != 0:
                if current_money > board_values[current_position]:
                    current_money -= board_values[current_position]
                    num_of_buying += 1
                    num_of_properties -= 1
                    possesions[current_position] = board_values[current_position] #add property to our list 
                    board_values[current_position] = 0 #buy that property and have it empty (value 0)
                
                    # else:
                    #     print("No sufficent funds to buy the property")


                    # print(f"throw {num_of_throw} position: {current_position} (property)")

                    # if num_of_buying == 1:
                    #     print(f"\n Player 1 has {num_of_buying} property in their possesion, There are still {num_of_properties}")
                    # elif num_of_buying == 28:
                    #     print("Player 1 has all properties")
                    # else:
                    #     print(f"\n Player 1 has {num_of_buying} properties in their possesion, There are still {num_of_properties}")
                    
        

        num_of_throw += 1
        previous_position = current_position
        current_position = throw_two_dice() + current_position

        if current_position < previous_position:
            current_money += 200
        #Wrap around the board using modulus to prevent index out of range
        current_position %= len(board_values)

        if current_position < previous_position:
            current_money += 200



    
    # print(f"Done! After throw {num_of_throw} the player owned all properties.")
    return num_of_throw



def simulate_monopoly_games(total_games: int, starting_money: int):
    throws_list = []  # List to track the number of throws in each game

    for game in range(total_games):
        number_of_throws = simulate_monopoly(starting_money)
        throws_list.append(number_of_throws)
    mean_of_throws = mean(throws_list)
    print(f"Monopoly simulator: 1 player, 1500 euros starting money, 2500 games. It took an average of {mean_of_throws} throws for the player to collect all streets")
    # print(throws_list)

  
    #Draw the graph (histogram)
    plt.hist(throws_list, bins=50, edgecolor='black')
    plt.title(f'Histogram of Throws in {total_games} Monopoly Games')
    plt.xlabel('Number of Throws')
    plt.ylabel('Frequency')
    plt.show()

    return mean_of_throws

# The following block ensures that the code only runs if this file is executed directly
if __name__ == "__main__":
    # Simulate 10,000 games
    simulate_monopoly_games(10000, 1500)