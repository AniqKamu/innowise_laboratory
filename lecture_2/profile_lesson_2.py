# Year used to calculate age
CURRENT_YEAR = 2025

# 1. Define a Function for the Profile & Calculations
def generate_profile(age: int) -> str:
    # Determines the user's life stage based on their age.
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        # For negative age or unforeseen circumstances
        return "N/A"

# 2. Get User Input
def get_user_data():
# Collects basic information and hobbies from the user.
    # Welcome the User and Get Basic Info
    print("Welcome to the Mini-Profile Generator!")

    # Request Full name
    user_name = input("Enter your full name: ")

    # Request year of birth and convert to int
    while True:
        birth_year_str = input("Enter your birth year: ")
        try:
            birth_year = int(birth_year_str)
            break
        except ValueError:
            print("Invalid input. Please enter a numerical year.")

    # Calculate the user's current age
    current_age = CURRENT_YEAR - birth_year

    # Gather Hobbies (A Flexible List)
    hobbies = []

    # Use a loop to repeatedly ask the user to enter a hobby
    while True:
        hobby_input = input("Enter a favorite hobby or type 'stop' to finish: ")

        # Check if the input is "stop" (case-insensitive)
        if hobby_input.lower() == "stop":
            break
        # If the input is not "stop" and not empty, add it to the list
        if hobby_input.strip():
            hobbies.append(hobby_input.strip())

    return user_name, birth_year, current_age, hobbies


# Main Program Flow
user_name, birth_year, current_age, hobbies = get_user_data()

# 3. Process and Generate the Profile
# Call generate_profile function
life_stage = generate_profile(current_age)

# Create a dictionary called user_profile
user_profile = {
    "name": user_name,
    "age": current_age,
    "birth_year": birth_year,
    "life_stage": life_stage,
    "hobbies": hobbies
}

# 4. Display the Output / Display the Final Profile
def display_profile(profile_data: dict):
# Displays a formatted profile summary.
    print("\n" + "---")
    print("Profile Summary:")

    # Print the user's name, current age, life stage
    print(f"Name: {profile_data['name']}")
    print(f"Age: {profile_data['age']}")
    print(f"Life Stage: {profile_data['life_stage']}")

    # Check if the hobbies list is empty
    if not profile_data['hobbies']:
        # If the list is empty, print a friendly message.
        print("You didn't mention any hobbies.")
    else:
        # If the list is not empty, print the total number of hobbies and then list each one.
        num_hobbies = len(profile_data['hobbies'])
        print(f"Favorite Hobbies ({num_hobbies}):")

        # Use a for loop to print each hobby on a new line, preceded by a bullet point (-).
        for hobby in profile_data['hobbies']:
            print(f"- {hobby}")

    print("---" + "\n")


# Derive the final profile
display_profile(user_profile)