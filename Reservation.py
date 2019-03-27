# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 3/26/19
# Python Version 3.7.3

# Importing pkgs
import os

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Tracks if the program is still running
Is_Running = True

# Stores the User's input
User_Input = ""

# Tracks if the User has made a decision
User_Confirm = False

# Tracks which seat the User has selected
Row_Selection = 0
Col_Selection = ""

#Tracks the specific ID of the seat that the User has selected
Seat_ID = ""

# Tracks the name of the person who has reserved the seat
Seat_Name = ""

# Dictionary that links reserved seats to a name
Reservations = {}

########################################################### PROGRAM LOGIC ################################################################

### The User wants to make a new reservation
def Add_Reservation():

    # Importing Global Variables
    global User_Input
    global User_Confirm
    global Row_Selection
    global Col_Selection

    while User_Confirm == False:

        User_Input = input("\nPlease select a row (1-25): ")
        if int(User_Input) > 0 and int(User_Input) < 26:
            Row_Selection = int(User_Input)

            while User_Confirm == False:
                User_Input = input("Please select a column (A-D): ")
                if User_Input.upper() == "A":
                    Col_Selection = "A"
                    break
                elif User_Input.upper() == "B":
                    Col_Selection = "B"
                    break
                elif User_Input.upper() == "C":
                    Col_Selection = "C"
                    break
                elif User_Input.upper() == "D":
                    Col_Selection = "D"
                    break
                else:
                    print("Please select a valid column.")
                    input("Press 'enter' to continue.")
            
            break

        else:
            print("Please enter a valid row.")
            input("Press 'enter' to continue.")

    Seat_ID = str(Row_Selection) + Col_Selection

    Seat_Name = input("Please enter the name for the reservation: ")

    print("\nSeat " + Seat_ID + " has been reserved for " + Seat_Name + ".")

    Reservations[Seat_ID] = Seat_Name

    print(Reservations)

    input("\nPress 'enter' to return to the main menu.")

### The User wants to cancel a reservation
def Del_Reservation():

    # Importing Global Variables
    global User_Input
    global User_Confirm

    input("Press 'enter' to return to the main menu.")

########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:

    while User_Confirm == False:

        # Clearing the screen to improve readability
        cls()

        print("Welcome to EZ Airline Reservation!")
        print("Please select one of the following options: ")

        print("""
        1. Reserve A Seat.
        2. Cancel A Reservation.
        3. Exit Program.""")

        User_Input = input("\nPlease enter your selection: ")

        # The User wants to make a new reservation
        if User_Input == "1": 
            Add_Reservation()
        # The User wants to cancel a reservation
        elif User_Input == "2": 
            Del_Reservation()
        # The User wants to close the program
        elif User_Input == "3": 
            Is_Running = False
            break
        # The User entered an invalid input
        else: 
            print("Please enter a valid selection.")
            input("Press 'enter' to continue.")
    