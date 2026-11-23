# Carpool Seat Matcher

A menu-driven Python program that helps drivers share rides and riders find and book seats. This is **Phase 1** of the project, built with procedural programming (functions, loops, conditions and dictionaries).

## Features

- Publish a trip with driver name, starting place, destination, time and free seats
- View all available trips
- Search trips by starting place and destination
- Book a seat (checks that the trip exists, a seat is free, and the rider has not already booked it)
- Cancel a booking (the seat becomes available again)
- View all bookings for a rider
- Sample trips are loaded at start so you can try it right away

## How it works

- `trips` dictionary stores trip details, keyed by trip number
- `bookings` dictionary stores bookings, keyed by booking number
- Input is checked so empty details or invalid numbers are not accepted

## How to run

1. Install Python 3 from [python.org](https://www.python.org/downloads/)
2. Download or clone this repository
3. Open a terminal in the project folder and run:

```
python carpool.py
```

## Menu

```
1. Publish a trip
2. View all trips
3. Search trips
4. Book a seat
5. Cancel a booking
6. View my bookings
7. Exit
```

## Sample search

Try searching from `Banashankari` to `PES University` to see the sample trips.

## Tech used

- Python 3 (no external libraries)

## Upcoming phases

- Phase 2: Object-oriented programming
- Phase 3: Error handling
- Phase 4: Flask front end

## Author

Tejaswini A
