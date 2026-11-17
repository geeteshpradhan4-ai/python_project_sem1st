# Movie Ticket Booking System

## About the Project

This is a simple movie ticket booking program made with Python. It runs in the terminal and lets a user book seats, cancel a booking, and check which seats are available.

The program has 3 rows (A, B, and C), with 5 seats in each row. Each ticket costs Rs. 200. When a seat is booked, the program saves it in a text file called `bookings.txt`. This means the booking information is still available the next time the program is run.

I made this project to practise Python basics such as functions, lists, loops, conditions, input validation, and file handling.

## Features

* Book one or more seats in a single request.
* Cancel a booked seat.
* View the seat map to check which seats are available or booked.
* Check that seat numbers are valid before booking.
* Prevent booking a seat that is already reserved.
* Prevent the same seat from being entered twice in one request.
* Save bookings in `bookings.txt` so they are available after restarting the program.
* Calculate the total ticket cost automatically.

## Seat Layout

There are 15 seats in total:

|Row|Seats|
|-|-|
|A|A1, A2, A3, A4, A5|
|B|B1, B2, B3, B4, B5|
|C|C1, C2, C3, C4, C5|

In the seat map:

* `0` means the seat is available.
* `1` means the seat is booked.

## Ticket Price

Each ticket costs **Rs. 200**.

For example, booking two seats costs:

`2 x Rs. 200 = Rs. 400`

## Requirements

* Python 3
* No third-party Python packages are required. The program uses Python's built-in `os` module.

## How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run the program:

```bash
   python movie\_booking.py
   ```

   On some systems, you may need to use:

```bash
   python3 movie\_booking.py
   ```

4. Follow the menu shown in the terminal.

## Menu Options

When the program starts, it displays these options:

```text
===== MOVIE TICKET BOOKING SYSTEM =====
1. Book Tickets
2. Cancel Booking
3. Seat Map
4. Exit
```

Choose an option by entering its number.

### Example: Booking Seats

Enter seat numbers separated by commas, like `A1,B2,C3`.

```text
Enter seat numbers to book (e.g. A1,B2,C3): A1,B2

Booking successful!
Seats booked: A1, B2
Amount payable: Rs. 400
```

### Example: Seat Map

If A1 and B2 are booked, the seat map will look like this:

```text
----- SEAT MAP -----
0 = Available, 1 = Booked
    1 2 3 4 5
A   1 0 0 0 0
B   0 1 0 0 0
C   0 0 0 0 0
```

### Example: Cancelling a Seat

Enter the seat number you want to cancel, such as `A1`. If it is booked, the program makes it available again.

## Project Files

```text
Movie-Ticket-Booking-System/
├── movie\_booking.py
├── README.md
└── bookings.txt   # Created automatically when a booking is saved
```

`bookings.txt` stores the booked seat numbers, one per line. You do not need to create it manually.


## Possible Improvements



* Let users choose a movie and show time.
* Generate a booking receipt.

## 

