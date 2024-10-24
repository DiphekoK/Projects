import random

def generate_secret_code(colors, code_length):
    return random.sample(colors, code_length)

def evaluate_guess(secret_code, player_guess):
    correct_position = sum(s == p for s, p in zip(secret_code, player_guess))
    correct_color = sum(min(secret_code.count(c), player_guess.count(c)) for c in set(player_guess)) - correct_position
    return correct_position, correct_color

def main():
    colors = ["red", "blue", "green", "yellow", "orange", "purple"]
    code_length = 4
    secret_code = generate_secret_code(colors, code_length)

    print("Welcome to Mastermind!")
    print("Try to guess the secret code made of the following colors:")
    print(", ".join(colors))
    print(f"You have one attempt to guess the 4-color code.")

    player_guess = input("Enter your guess (separate colors with spaces): ").strip().lower().split()

    if len(player_guess) != code_length:
        print(f"Please enter exactly 4 colors.")
        main()

    correct_position, correct_color = evaluate_guess(secret_code, player_guess)

    print(f"Your guess: {player_guess}")
    print(f"Correct colors in the correct position: {correct_position}")
    print(f"Correct colors in the wrong position: {correct_color}")
    print(f"The secret code was: {secret_code}")

if __name__ == "__main__":
    main()


