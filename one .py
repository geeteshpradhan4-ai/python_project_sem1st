
import os

TICKET_PRICE = 200
ROWS = ["A", "B", "C"]
SEATS_PER_ROW = 5
FILENAME = "bookings.txt"

# 0 = Available, 1 = Booked
seats = [[0, 0, 0, 0, 0] for _ in ROWS]

# Stores seat number and customer name
booked_name = {}


# Load previous bookings
def load_bookings():
    if os.path.exists(FILENAME):
        file = open(FILENAME, "r")

        for line in file:
            data = line.strip().split(",", 1)

            if len(data) == 2:
                seat = data[0].upper()
                name = data[1]

                if len(seat) == 2 and seat[0] in ROWS and seat[1].isdigit():
                    row = ROWS.index(seat[0])
                    column = int(seat[1]) - 1

                    if 0 <= column < SEATS_PER_ROW:
                        seats[row][column] = 1
                        booked_name[seat] = name

        file.close()


# Save bookings
def save_bookings():
    file = open(FILENAME, "w")

    for row in range(len(ROWS)):
        for column in range(SEATS_PER_ROW):
            seat = ROWS[row] + str(column + 1)

            if seats[row][column] == 1:
                file.write(seat + "," + booked_name[seat] + "\n")

    file.close()


# Count available seats
def seats_left():
    total = 0

    for row in range(len(ROWS)):
        for column in range(SEATS_PER_ROW):
            if seats[row][column] == 0:
                total += 1

    return total


# Display seat map
def display_seat_map():
    print("\n----- SEAT MAP -----")

    for row in range(len(ROWS)):
        print("Row", ROWS[row] + ":", end=" ")

        for column in range(SEATS_PER_ROW):
            if seats[row][column] == 1:
                print("X", end=" ")
            else:
                print("_", end=" ")

        print()

    print("Seats left:", seats_left())


# Book single or multiple seats
def book_seat():
    seat_input = input(
        "Enter seat(s) to book, like A1 or A2,A3: "
    ).upper().strip()

    seat_list = seat_input.replace(",", " ").split()

    if not seat_list:
        print("Invalid seat number.")
        return

    # Check for duplicate seat entries
    if len(seat_list) != len(set(seat_list)):
        print("Duplicate seat entered.")
        return

    # Validate all seats before booking
    for seat in seat_list:

        if (len(seat) != 2 or
            seat[0] not in ROWS or
            not seat[1].isdigit()):

            print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
            return

        row = ROWS.index(seat[0])
        column = int(seat[1]) - 1

        if column < 0 or column >= SEATS_PER_ROW:
            print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
            return

        if seats[row][column] == 1:
            print("Seat", seat, "is already booked.")
            return

    # Check customer name
    name = input("Enter customer name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    # Book all selected seats
    for seat in seat_list:
        row = ROWS.index(seat[0])
        column = int(seat[1]) - 1

        seats[row][column] = 1
        booked_name[seat] = name

    save_bookings()

    amount = len(seat_list) * TICKET_PRICE

    # Display booking confirmation
    if len(seat_list) == 1:
        print("Seat", seat_list[0], "booked for", name + ".", "Amount:", amount)
    else:
        print("Seats", ", ".join(seat_list), "booked for", name + ".", "Amount:", amount)

    print("Seats left:", seats_left())

    if seats_left() == 0:
        print("Show is now housefull.")


# Cancel booking
def cancel_booking():
    seat = input("Enter a seat to cancel, like A1: ").upper().strip()

    if len(seat) != 2 or seat[0] not in ROWS or not seat[1].isdigit():
        print("Invalid seat number.")
        return

    row = ROWS.index(seat[0])
    column = int(seat[1]) - 1

    if column < 0 or column >= SEATS_PER_ROW:
        print("Invalid seat number.")

    elif seats[row][column] == 0:
        print("That seat is not booked.")

    else:
        print("Booking cancelled for:", booked_name[seat])

        seats[row][column] = 0
        del booked_name[seat]

        save_bookings()

        print("Booking cancelled successfully.")
        print("Seats left:", seats_left())


# Main menu
def main():
    load_bookings()

    while True:
        print("\n===== MOVIE TICKET BOOKING SYSTEM =====")
        print("1. Book a seat")
        print("2. Cancel a booking")
        print("3. Show seat map")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            book_seat()

        elif choice == "2":
            cancel_booking()

        elif choice == "3":
            display_seat_map()

        elif choice == "4":
            print("Dhanyavaad!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
