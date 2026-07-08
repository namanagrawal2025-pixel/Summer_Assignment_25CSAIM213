def view_seats(seats):
    for seat, status in seats.items():
        print("Seat", seat, ":", status)

def book_seat(seats):
    seat_num = input("Enter seat number to book (1-5): ")
    if seat_num in seats:
        if seats[seat_num] == "Available":
            seats[seat_num] = "Booked"
            print("Seat booked successfully!")
        else:
            print("Seat is already booked.")
    else:
        print("Invalid seat number.")

def booking_system():
    seats = {"1": "Available", "2": "Available", "3": "Available", "4": "Available", "5": "Available"}
    while True:
        print("\n1. View Seats\n2. Book Seat\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            view_seats(seats)
        elif choice == "2":
            book_seat(seats)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    booking_system()

main()
