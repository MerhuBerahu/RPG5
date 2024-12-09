

# Function to validate user input
def get_valid_choice(i):
    while True:
        try:
            user_input = int(input("Enter the number of your choice: "))
            if 1 <= user_input <= len(i):
                return user_input
            else:
                print(f"Please enter a number between 1 and {len(i)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")