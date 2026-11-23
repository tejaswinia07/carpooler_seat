trips = {}      
bookings = {}   


counters = {"trip": 1, "booking": 1}



def read_number(message):
    while True:
        text = input(message).strip()
        if text.isdigit():
            return int(text)
        print("Please enter a valid number.")


def same_text(a, b):
    return a.strip().lower() == b.strip().lower()


def add_trip(driver, source, destination, time, seats):
    trip_id = counters["trip"]
    trips[trip_id] = {
        "driver": driver,
        "source": source,
        "destination": destination,
        "time": time,
        "total_seats": seats,
        "seats_left": seats,
    }
    counters["trip"] += 1
    return trip_id


def print_trip(trip_id, trip):
    print(f"  Trip {trip_id}: {trip['source']} -> {trip['destination']} | "
          f"Time: {trip['time']} | Driver: {trip['driver']} | "
          f"Seats left: {trip['seats_left']}/{trip['total_seats']}")



def load_sample_data():
    add_trip("Teju", "Banashankari", "PES University", "08:00 AM", 3)
    add_trip("Vidushi", "Jayanagar", "Electronic City", "09:30 AM", 2)
    add_trip("Tripthi", "Banashankari", "PES University", "08:30 AM", 1)
    add_trip("Revathi", "Kengeri", "Majestic", "07:45 AM", 4)


def show_menu():
    print("\n===== Carpool Seat Matcher =====")
    print("1. Publish a trip")
    print("2. View all trips")
    print("3. Search trips")
    print("4. Book a seat")
    print("5. Cancel a booking")
    print("6. View my bookings")
    print("7. Exit")


def publish_trip():
    print("\n--- Publish a trip ---")
    driver = input("Driver name: ").strip()
    source = input("Starting place: ").strip()
    destination = input("Destination: ").strip()
    time = input("Departure time (e.g. 08:00 AM): ").strip()
    seats = read_number("Number of free seats: ")

    if driver == "" or source == "" or destination == "" or time == "":
        print("All details are required. Trip not published.")
        return
    if seats <= 0:
        print("Seats must be more than 0. Trip not published.")
        return

    trip_id = add_trip(driver, source, destination, time, seats)
    print(f"Trip published. Your trip number is {trip_id}.")


def view_trips():
    print("\n--- All trips ---")
    if len(trips) == 0:
        print("No trips available.")
        return
    for trip_id, trip in trips.items():
        print_trip(trip_id, trip)


def search_trips():
    print("\n--- Search trips ---")
    source = input("Starting place: ").strip()
    destination = input("Destination: ").strip()

    found = False
    for trip_id, trip in trips.items():
        if (same_text(trip["source"], source)
                and same_text(trip["destination"], destination)
                and trip["seats_left"] > 0):
            print_trip(trip_id, trip)
            found = True

    if not found:
        print("No trips found.")


def book_seat():
    print("\n--- Book a seat ---")
    rider = input("Your name: ").strip()
    if rider == "":
        print("Name is required.")
        return
    trip_id = read_number("Trip number: ")

    # Check 1: does the trip exist?
    if trip_id not in trips:
        print("Trip not found.")
        return

    trip = trips[trip_id]

    # Check 2: is at least one seat free?
    if trip["seats_left"] <= 0:
        print("No seats left on this trip.")
        return

    # Check 3: same rider cannot book the same trip twice
    for booking in bookings.values():
        if (same_text(booking["rider"], rider)
                and booking["trip_id"] == trip_id
                and booking["status"] == "confirmed"):
            print("You have already booked this trip.")
            return

    # All fine: reduce seat and save booking
    trip["seats_left"] -= 1
    booking_id = counters["booking"]
    bookings[booking_id] = {"rider": rider, "trip_id": trip_id, "status": "confirmed"}
    counters["booking"] += 1
    print(f"Seat booked! Your booking number is {booking_id}.")


def cancel_booking():
    print("\n--- Cancel a booking ---")
    booking_id = read_number("Booking number: ")

    if booking_id not in bookings:
        print("Booking not found.")
        return

    booking = bookings[booking_id]
    if booking["status"] == "cancelled":
        print("This booking is already cancelled.")
        return

    booking["status"] = "cancelled"
    trips[booking["trip_id"]]["seats_left"] += 1
    print("Booking cancelled. The seat is available again.")


def view_bookings():
    print("\n--- My bookings ---")
    rider = input("Your name: ").strip()

    found = False
    for booking_id, booking in bookings.items():
        if same_text(booking["rider"], rider):
            trip = trips[booking["trip_id"]]
            print(f"  Booking {booking_id}: Trip {booking['trip_id']} "
                  f"({trip['source']} -> {trip['destination']}, {trip['time']}) "
                  f"| Status: {booking['status']}")
            found = True

    if not found:
        print("No bookings found for this name.")


def main():
    load_sample_data()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            publish_trip()
        elif choice == "2":
            view_trips()
        elif choice == "3":
            search_trips()
        elif choice == "4":
            book_seat()
        elif choice == "5":
            cancel_booking()
        elif choice == "6":
            view_bookings()
        elif choice == "7":
            print("Thank you for using Carpool Seat Matcher. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()