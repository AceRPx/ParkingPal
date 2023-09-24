
# Define available parking lots and their capacities
parking_lots = {
    'Red': 3,
    'Blue': 3,
    'Green': 3,
}

# Function to display available parking lots
def display_available_lots():
    print("Available Parking Lots:")
    for color, spaces in parking_lots.items():
        print(f"{color} - {spaces} spaces")

# Function to park in a selected lot
def park_car(selected_lot):
    if selected_lot in parking_lots and parking_lots[selected_lot] > 0:
        parking_lots[selected_lot] -= 1
        print(f"You have parked your car in the {selected_lot} lot.")
    else:
        print("Sorry, the selected lot is full or invalid.")

# Main loop
while True:
    display_available_lots()

    # Get user input
    selected_color = input("Select a parking lot color (or 'quit' to exit): ").capitalize()

    if selected_color == 'Quit':
        break

    park_car(selected_color)

# Final display of available parking lots
print("Thank you for using the parking lot app.")
display_available_lots()
