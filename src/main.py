import sqlite3
def menu():
    while True:
        print("\n==============================")
        print(" VEHICLE RENTAL SYSTEM")
        print("==============================")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Search Vehicle")
        print("4. Rent Vehicle")
        print("5. Return Vehicle")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
           add_vehicle()

        elif choice == "2":
          view_vehicles()

        elif choice == "3":
            print("Search Vehicle selected")

        elif choice == "4":
            print("Rent Vehicle selected")

        elif choice == "5":
            print("Return Vehicle selected")

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")

def add_vehicle():

    connection = sqlite3.connect("database/vehicle_rental.db")
    cursor = connection.cursor()

    vehicle_name = input("Enter Vehicle Name: ")
    vehicle_type = input("Enter Vehicle Type: ")
    brand = input("Enter Brand: ")
    price = float(input("Enter Price Per Day: "))

    cursor.execute("""
    INSERT INTO Vehicles
    (vehicle_name, vehicle_type, brand, price_per_day, status)
    VALUES (?, ?, ?, ?, ?)
    """,
    (vehicle_name, vehicle_type, brand, price, "Available"))

    connection.commit()
    connection.close()

    print("\nVehicle Added Successfully!")

def view_vehicles():

    connection = sqlite3.connect("database/vehicle_rental.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Vehicles")

    vehicles = cursor.fetchall()

    print("\n========== VEHICLES ==========\n")

    for vehicle in vehicles:
        print(vehicle)

    connection.close()

def add_vehicle():
    connection = sqlite3.connect("database/vehicle_rental.db")
    cursor = connection.cursor()

    vehicle_name = input("Enter Vehicle Name: ")
    vehicle_type = input("Enter Vehicle Type (Car/Bike): ")
    brand = input("Enter Brand: ")
    price = float(input("Enter Price Per Day: "))

    cursor.execute("""
        INSERT INTO Vehicles
        (vehicle_name, vehicle_type, brand, price_per_day, status)
        VALUES (?, ?, ?, ?, ?)
    """, (vehicle_name, vehicle_type, brand, price, "Available"))

    connection.commit()
    connection.close()

    print("\n✅ Vehicle Added Successfully!")

def add_vehicle():
    connection = sqlite3.connect("database/vehicle_rental.db")
    cursor = connection.cursor()

    vehicle_name = input("Enter Vehicle Name: ")
    vehicle_type = input("Enter Vehicle Type (Car/Bike): ")
    brand = input("Enter Brand: ")
    price = float(input("Enter Price Per Day: "))

    cursor.execute("""
    INSERT INTO Vehicles
    (vehicle_name, vehicle_type, brand, price_per_day, status)
    VALUES (?, ?, ?, ?, ?)
    """, (vehicle_name, vehicle_type, brand, price, "Available"))

    connection.commit()
    connection.close()

    print("\n✅ Vehicle Added Successfully!")

def view_vehicles():

    connection = sqlite3.connect("database/vehicle_rental.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Vehicles")

    vehicles = cursor.fetchall()

    if len(vehicles) == 0:
        print("\nNo vehicles found.")
    else:
        print("\n========== VEHICLE LIST ==========\n")

        for vehicle in vehicles:
            print(f"""
Vehicle ID      : {vehicle[0]}
Vehicle Name    : {vehicle[1]}
Vehicle Type    : {vehicle[2]}
Brand           : {vehicle[3]}
Price Per Day   : ₹{vehicle[4]}
Status          : {vehicle[5]}
----------------------------------------
""")

    connection.close()
menu()