import random
import matplotlib.pyplot as plt
from statistics import mean

# Function to simulate rolling two dice
def throw_two_dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1 + dice_2

# Function to simulate a Monopoly game with two players
def simulate_monopoly(starting_money_p1, starting_money_p2):
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]  # Board setup

    possession_count_p1 = 0  # Player 1 property count
    possession_count_p2 = 0  # Player 2 property count

    current_position_p1, current_position_p2 = 0, 0
    current_money_p1, current_money_p2 = starting_money_p1, starting_money_p2
    num_of_properties = 28  # Total properties available to buy

    while sum(board_values) != 0:  # Game loop

        # Player 1's turn
        previous_position_p1 = current_position_p1
        current_position_p1 = (current_position_p1 + throw_two_dice()) % len(board_values)

        # Check if Player 1 passes or lands on GO
        if current_position_p1 < previous_position_p1:
            current_money_p1 += 200  # Collect $200 for passing GO

        # Check if Player 1 can buy the property
        if board_values[current_position_p1] != 0 and current_money_p1 >= board_values[current_position_p1]:
            current_money_p1 -= board_values[current_position_p1]
            possession_count_p1 += 1  # Player 1 buys the property
            board_values[current_position_p1] = 0  # Mark the property as bought

        # Player 2's turn
        previous_position_p2 = current_position_p2
        current_position_p2 = (current_position_p2 + throw_two_dice()) % len(board_values)

        # Check if Player 2 passes or lands on GO
        if current_position_p2 < previous_position_p2:
            current_money_p2 += 200  # Collect $200 for passing GO

        # Check if Player 2 can buy the property
        if board_values[current_position_p2] != 0 and current_money_p2 >= board_values[current_position_p2]:
            current_money_p2 -= board_values[current_position_p2]
            possession_count_p2 += 1  # Player 2 buys the property
            board_values[current_position_p2] = 0  # Mark the property as bought

    # Return the difference in properties between Player 1 and Player 2
    return possession_count_p1 - possession_count_p2

# Function to simulate multiple Monopoly games
def simulate_monopoly_games(total_games, starting_money_p1, starting_money_p2):
    possession_differences = []  # Track the difference in possessions between players

    for game in range(total_games):
        delta = simulate_monopoly(starting_money_p1, starting_money_p2)
        possession_differences.append(delta)

    # Calculate the average difference
    average_difference = mean(possession_differences)

    print(f"Monopoly simulator: two players, {starting_money_p1} euros starting money, {total_games} games.")
    print(f"On average player 1 has {average_difference:.2f} more streets in their possession when all streets are bought.")

    # Plot histogram of possession differences
    plt.hist(possession_differences, bins=50, edgecolor='black')
    plt.title(f"Histogram of Property Differences in {total_games} Monopoly Games")
    plt.xlabel("Possession Difference (Player 1 - Player 2)")
    plt.ylabel("Frequency")
    plt.show()

    return average_difference


def equilibrium(total_games):
    starting_money_p1 = 1500  # Player 1 starting money
    extra_money_options = [0, 50, 100, 150, 200]  # Extra money for Player 2
    differences = []

    for extra_money in extra_money_options:
        starting_money_p2 = 1500 + extra_money  # Player 2 starts with more money
        average_difference = simulate_monopoly_games(total_games, starting_money_p1, starting_money_p2)
        differences.append(average_difference)

        # Print the result in the required format
        print(f"Starting money [1500,{starting_money_p2}]: player 1 on average {average_difference:.2f} more streets (player 2 got {extra_money} extra starting money)")

    # Plotting the results
    plt.plot(extra_money_options, differences, marker='o')
    plt.title("Average Difference in Properties (Player 1 - Player 2)")
    plt.xlabel("Extra Starting Money for Player 2")
    plt.ylabel("Average Difference in Properties")
    plt.grid(True)
    plt.show()


# Run the equilibrium test
if __name__ == "__main__":
    equilibrium(10000)