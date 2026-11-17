import os

TICKET_PRICE = 200
ROWS = ["A", "B", "C"]
SEATS_PER_ROW = 5
FILENAME = "bookings.txt"

# 0 means available; 1 means booked
seats = [[0, 0, 0, 0, 0] for _ in ROWS]


def load_bookings():
    if os.path.exists(FILENAME):
        file = open(FILENAME, "r")

        for line in file:
            seat = line.strip()

            if len(seat) == 2 and seat[0] in ROWS and seat[1].isdigit():
                row = ROWS.index(seat[0])
                column = int(seat[1]) - 1

                if column >= 0 and column < SEATS_PER_ROW:
                    seats[row][column] = 1

        file.close()


def save_bookings():
    file = open(FILENAME, "w")

    for row in range(len(ROWS)):
        for column in range(SEATS_PER_ROW):
            if seats[row][column] == 1:
                file.write(ROWS[row] + str(column + 1) + "\n")

    file.close()


def display_seat_map():
    print("\n----- SEAT MAP -----")
    print("0 = Available, 1 = Booked")
    print("    1 2 3 4 5")

    for row in range(len(ROWS)):
        print(ROWS[row], " ", end="")

        for column in range(SEATS_PER_ROW):
            print(seats[row][column], end=" ")

        print()


def book_seat():
    seat = input("Enter a seat to book, like A1: ").upper().strip()

    if len(seat) != 2 or seat[0] not in ROWS or not seat[1].isdigit():
        print("Invalid seat number.")
        return

    row = ROWS.index(seat[0])
    column = int(seat[1]) - 1

    if column < 0 or column >= SEATS_PER_ROW:
        print("Invalid seat number.")
    elif seats[row][column] == 1:
        print("That seat is already booked.")
    else:
        seats[row][column] = 1
        save_bookings()
        print("Booking successful!")
        print("Amount payable: Rs.", TICKET_PRICE)


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
        seats[row][column] = 0
        save_bookings()
        print("Booking cancelled successfully.")


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