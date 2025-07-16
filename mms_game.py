def start_game():
    
    max_attempts = 5
    target = np.random.randint(1, 201)
    attempts= 0
    
    print("Welcome to the M&Ms Guessing Game!")
    print(f"You have {max_attempts} guesses to find out how many M&Ms are in the jar.")
    #print("There are 42 M&Ms in the jar.")  # Hardcoded number
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1
        remaining = max_attempts - attempts
        print(f"You guessed {guess}.", end=' ')

        if guess < target:
            print("Too low!", end=' ')
        elif guess > target:
            print("Too high!", end=' ')
        else:
            print(f"You got it in {attempts} {'try' if attempts == 1 else 'tries'}!")
            return

        if remaining > 0:
            print(f"You have {remaining} {'guess' if remaining == 1 else 'guesses'} left.")
        else:
            print(f"Sorry, you've used all your attempts. The correct number was {target}.")
    
    #print("You guessed 50.")               # Hardcoded guess
    print("Sorry, that's too high!")       # Hardcoded feedback

if __name__ == "__main__":
    start_game()