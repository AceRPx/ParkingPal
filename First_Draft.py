
# Define available parking lots and their capacities
parking_lots = {
    'Red': 5,
    'Blue': 5,
    'Green': 5,
}

# Initialize a dictionary to track occupied slots in each lot
occupied_slots = {
    'Red': [],
    'Blue': [],
    'Green': [],
}
# Function to display available parking lots
def display_available_lots():
    print("Available Parking Lots:")
    for color, spaces in parking_lots.items():
        available_spaces = spaces - len(occupied_slots[color])
        print(f"{color} - {available_spaces}/{spaces} spaces")

# Function to park in a selected lot
def park_car(selected_lot):
    if selected_lot not in parking_lots or parking_lots[selected_lot] <= 0:
        print(f"Sorry, the {selected_lot} lot is full or invalid.")
        return False

    name = input("Enter your name: ")
    
#Email Verification
    email = input("Enter your email (must be @my.erau.edu or @erau.edu): ")

    email_pattern = r"^[a-zA-Z0-9_.+-]+@(my\.)?erau\.edu$"
    if not re.match(email_pattern, email):
        print("Invalid email format. Please use @my.erau.edu or @erau.edu.")
        return False

# Menu program
while True:
    print("Options:")
    print("1. Clear Storage")
    print("2. Park Car")
    print("3. Quit")
    
    option = input("Select an option (1/2/3): ")
    
    if option == '1':
        clear_storage()
    elif option == '2':
        display_available_lots()
        selected_color = input("Select a parking lot color (or 'quit' to exit): ").capitalize()
        if selected_color == 'Quit':
            break
        parked = park_car(selected_color)
        if parked:
            print("User Information:")
            values = worksheet.get_all_values()
            for row in values:
                print(f"Name: {row[0]}, Email: {row[1]}, Selected Color: {row[2]}")
    elif option == '3':
        break

print("Thank you for using the parking lot app.")
