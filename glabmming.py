import random
import time

# User data storage
users = {}

# Function to display current balance
def display_balance(balance):
    print(f"Your current balance: ${balance}")

# Function to register a new user
def register():
    print("Register")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please login or choose another username.")
        return None, None
    password = input("Enter a password: ")
    users[username] = {'password': password, 'balance': 0}
    print("Registration successful! Please login.")
    return username

# Function to login an existing user
def login():
    print("Login")
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return None, None
    password = input("Enter your password: ")
    if users[username]['password'] != password:
        print("Incorrect password.")
        return None, None
    print("Login successful!")
    return username, users[username]['balance']

# Function to add money to user's balance
def add_balance(username):
    amount = float(input("Enter the amount of money to add to your balance: $"))
    users[username]['balance'] += amount
    print(f"${amount} has been added to your balance.")
    return users[username]['balance']

# Function to play Aviator
def play_aviator(balance):
    while True:
        print("\n--- Aviator Game ---")
        bet = float(input("Enter your bet: $"))
        if bet > balance:
            print("You don't have enough money!")
        else:
            crash_point = random.uniform(1.5, 10)  # Crash point between 1.5x and 10x
            multiplier = 1.0
            print("The multiplier is increasing...")
            while multiplier < crash_point:
                print(f"Multiplier: {multiplier:.2f}x", end="\r")
                time.sleep(0.2)
                multiplier += random.uniform(0.1, 0.5)
            print(f"\nThe multiplier crashed at {multiplier:.2f}x!")
            cash_out = input("Do you want to cash out? (y/n): ").lower()
            if cash_out == 'y':
                winnings = bet * multiplier
                print(f"You cashed out at {multiplier:.2f}x. You won ${winnings:.2f}")
                balance += winnings
            else:
                print("You chose to not cash out. You lost your bet.")
                balance -= bet
        print(f"Your new balance is: ${balance:.2f}")
        play_again = input("Do you want to play Aviator again? (y/n): ").lower()
        if play_again != 'y':
            break
    return balance

# Function to play Color Prediction
def play_color_prediction(balance):
    while True:
        print("\n--- Color Prediction Game ---")
        bet = float(input("Enter your bet: $"))
        if bet > balance:
            print("You don't have enough money!")
        else:
            prediction = input("Predict the color (red/black): ").lower()
            outcome = random.choice(["red", "black"])
            if prediction == outcome:
                print(f"Congratulations! The color was {outcome}. You won ${bet * 2}.")
                balance += (bet * 2)
            else:
                print(f"The color was {outcome}. You lost ${bet}.")
                balance -= bet
        print(f"Your new balance is: ${balance:.2f}")
        play_again = input("Do you want to play Color Prediction again? (y/n): ").lower()
        if play_again != 'y':
            break
    return balance

# Function to play 7 Up 7 Down Dice Game
def play_seven_up_seven_down(balance):
    while True:
        print("\n--- 7 Up 7 Down Game ---")
        bet = float(input("Enter your bet: $"))
        if bet > balance:
            print("You don't have enough money!")
        else:
            print("Predict the outcome:")
            print("1. Below 7")
            print("2. Above 7")
            print("3. Exactly 7")
            choice = input("Enter your choice (1/2/3): ")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice_sum = dice1 + dice2
            print(f"Dice roll: {dice1} + {dice2} = {dice_sum}")
            if choice == "1" and dice_sum < 7:
                print(f"You win ${bet * 2}.")
                balance += (bet * 2)
            elif choice == "2" and dice_sum > 7:
                print(f"You win ${bet * 2}.")
                balance += (bet * 2)
            elif choice == "3" and dice_sum == 7:
                print(f"You win ${bet * 3}.")
                balance += (bet * 3)
            else:
                print(f"You lost ${bet}.")
                balance -= bet
        print(f"Your new balance is: ${balance:.2f}")
        play_again = input("Do you want to play 7 Up 7 Down again? (y/n): ").lower()
        if play_again != 'y':
            break
    return balance

# Main Menu and Game Loop
def main():
    username = None
    balance = 0
    while True:
        print("\n--- Welcome to the Gambling Game ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            username = register()
            if username:
                username, balance = login()
                if username:
                    break
        elif choice == "2":
            username, balance = login()
            if username:
                break
        elif choice == "3":
            print("Thanks for visiting!")
            return
        else:
            print("Invalid choice. Please try again.")
    balance = add_balance(username)
    while balance > 0:
        print("\n--- Gambling Game ---")
        print("1. Play Aviator")
        print("2. Play Color Prediction")
        print("3. Play 7 Up 7 Down")
        print("4. Exit")
        display_balance(balance)
        choice = input("Choose a game (1/2/3/4): ")
        if choice == "1":
            balance = play_aviator(balance)
        elif choice == "2":
            balance = play_color_prediction(balance)
        elif choice == "3":
            balance = play_seven_up_seven_down(balance)
        elif choice == "4":
            print("Thanks for playing!")
            users[username]['balance'] = balance
            break
        else:
            print("Invalid choice. Please try again.")
    if balance <= 0:
        print("You ran out of money. Game over.")
        users[username]['balance'] = 0

# Start the game
if __name__ == "__main__":
    main()