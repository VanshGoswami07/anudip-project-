import sqlite3 
from datetime import datetime

# ==========================
# INPUT VALIDATION FUNCTIONS
# ==========================

def get_integer(message):

    while True:

        value = input(message).strip()

        try:
            return int(value)

        except ValueError:
            print("\nInvalid input! Please enter a whole number.")


def get_float(message):

    while True:

        value = input(message).strip()

        try:

            value = float(value)

            if value <= 0:
                print("\nValue must be greater than 0.")
                continue

            return value

        except ValueError:
            print("\nInvalid input! Please enter a valid number.")


def get_text(message):

    while True:

        value = input(message).strip()

        if value == "":
            print("\nThis field cannot be empty.")

        else:
            return value

# ==========================
# DATABASE CONNECTION
# ==========================

def get_connection():
    return sqlite3.connect("database/vehicle_rental.db")


# ==========================
# MAIN MENU
# ==========================

def menu():

    while True:
        dashboard()

        print("\n===================================")
        print("     VEHICLE RENTAL SYSTEM")
        print("===================================")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Search Vehicle")
        print("4. Add Customer")
        print("5. View Customers")
        print("6. Search Customer")
        print("7. Rent Vehicle")
        print("8. Return Vehicle")
        print("9. Rental History")
        print("10. Update Vehicle")
        print("11. Delete Vehicle")
        print("12. Update Customer")
        print("13. Delete Customer")
        print("14. Generate Bill")
        print("15. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_vehicle()

        elif choice == "2":
            view_vehicles()

        elif choice == "3":
            search_vehicle()

        elif choice == "4":
            add_customer()

        elif choice == "5":
            view_customers()

        elif choice == "6":
            search_customer()

        elif choice == "7":
            rent_vehicle()

        elif choice == "8":
            return_vehicle()

        elif choice == "9":
            rental_history()  

        elif choice == "10":
            update_vehicle()
            
        elif choice == "11": 
            delete_vehicle()

        elif choice == "12":
           update_customer()

        elif choice == "13":
           delete_customer()
        elif choice == "14":
           generate_bill()

        elif choice == "15":
            print("\nThank You!")
            break

        else:
            print("\nInvalid Choice!")


# ==========================
# VEHICLE FUNCTIONS
# ==========================

def add_vehicle():

    connection = get_connection()
    cursor = connection.cursor()

    vehicle_name = get_text("Enter Vehicle Name: ")
    vehicle_type = get_text("Enter Vehicle Type (Car/Bike): ")
    brand = get_text("Enter Brand: ")
    price = get_float("Enter Price Per Day: ")

    try:
        cursor.execute("""
        INSERT INTO Vehicles
        (vehicle_name, vehicle_type, brand, price_per_day, status)
        VALUES (?, ?, ?, ?, ?)
        """, (vehicle_name, vehicle_type, brand, price, "Available"))

        connection.commit()
        print("\n✅ Vehicle Added Successfully!")

    except sqlite3.Error as e:
        print(f"\nDatabase Error: {e}")

    finally:
        connection.close()

def view_vehicles():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Vehicles")
    vehicles = cursor.fetchall()

    if len(vehicles) == 0:
        print("\nNo Vehicles Found.")

    else:

        print("\n========== VEHICLE LIST ==========\n")

        print("=" * 80)
        print(f"{'ID':<5}{'Vehicle Name':<20}{'Type':<12}{'Brand':<15}{'Price':<12}{'Status'}")
        print("=" * 80)

        for vehicle in vehicles:
            print(
                f"{vehicle[0]:<5}"
                f"{vehicle[1]:<20}"
                f"{vehicle[2]:<12}"
                f"{vehicle[3]:<15}"
                f"₹{vehicle[4]:<11.2f}"
                f"{vehicle[5]}"
            )

        print("=" * 80)

    connection.close()


def search_vehicle():

    connection = get_connection()
    cursor = connection.cursor()

    keyword = input(
        "Enter Vehicle ID, Name, Brand or Type: "
    ).strip()

    if keyword == "":
        print("\nSearch field cannot be empty.")
        connection.close()
        return

    cursor.execute("""
    SELECT * FROM Vehicles
    WHERE
        CAST(vehicle_id AS TEXT) LIKE ?
        OR vehicle_name LIKE ?
        OR brand LIKE ?
        OR vehicle_type LIKE ?
    """,
    (
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%'
    ))

    vehicles = cursor.fetchall()

    if len(vehicles) == 0:
        print("\nNo Vehicle Found.")

    else:

        print("\n========== SEARCH RESULT ==========\n")

        print("=" * 80)
        print(f"{'ID':<5}{'Vehicle Name':<20}{'Type':<12}{'Brand':<15}{'Price':<12}{'Status'}")
        print("=" * 80)

        for vehicle in vehicles:

            print(
                f"{vehicle[0]:<5}"
                f"{vehicle[1]:<20}"
                f"{vehicle[2]:<12}"
                f"{vehicle[3]:<15}"
                f"₹{vehicle[4]:<11.2f}"
                f"{vehicle[5]}"
            )

        print("=" * 80)

    connection.close()



# ==========================
# CUSTOMER FUNCTIONS
# ==========================

def add_customer():

    connection = get_connection()
    cursor = connection.cursor()

    customer_name = get_text("Enter Customer Name: ")

    while True:

        phone_number = input("Enter Phone Number: ").strip()

        if phone_number.isdigit() and len(phone_number) == 10:
            break

        print("\nPhone number must contain exactly 10 digits.")

    email = get_text("Enter Email: ")

    driving_license = get_text("Enter Driving License Number: ")

    try:

        cursor.execute("""
        INSERT INTO Customers
        (customer_name, phone_number, email, driving_license)
        VALUES (?, ?, ?, ?)
        """, (customer_name, phone_number, email, driving_license))

        connection.commit()

        print("\n✅ Customer Added Successfully!")

    except sqlite3.Error as e:

        print(f"\nDatabase Error: {e}")

    finally:

        connection.close()

def view_customers():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Customers")
    customers = cursor.fetchall()

    if len(customers) == 0:
        print("\nNo Customers Found.")

    else:

        print("\n========== CUSTOMER LIST ==========\n")

        print("=" * 100)
        print(f"{'ID':<5}{'Customer Name':<20}{'Phone':<15}{'Email':<35}{'License'}")
        print("=" * 100)

        for customer in customers:
            print(
                f"{customer[0]:<5}"
                f"{customer[1]:<20}"
                f"{customer[2]:<15}"
                f"{customer[3]:<35}"
                f"{customer[4]}"
            )

        print("=" * 100)

    connection.close()

def search_customer():

    connection = get_connection()
    cursor = connection.cursor()

    keyword = input(
        "Enter Customer ID, Name, Phone or License: "
    ).strip()

    if keyword == "":
        print("\nSearch field cannot be empty.")
        connection.close()
        return

    cursor.execute("""
    SELECT * FROM Customers
    WHERE
        CAST(customer_id AS TEXT) LIKE ?
        OR customer_name LIKE ?
        OR phone_number LIKE ?
        OR driving_license LIKE ?
    """,
    (
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%'
    ))

    customers = cursor.fetchall()

    if len(customers) == 0:
        print("\nNo Customer Found.")

    else:

        print("\n========== SEARCH RESULT ==========\n")

        print("=" * 100)
        print(f"{'ID':<5}{'Customer Name':<20}{'Phone':<15}{'Email':<35}{'License'}")
        print("=" * 100)

        for customer in customers:

            print(
                f"{customer[0]:<5}"
                f"{customer[1]:<20}"
                f"{customer[2]:<15}"
                f"{customer[3]:<35}"
                f"{customer[4]}"
            )

        print("=" * 100)

    connection.close()
# ==========================
# RENT VEHICLE
# ==========================

def rent_vehicle():

    connection = get_connection()
    cursor = connection.cursor()

    customer_id = input("Enter Customer ID: ")
    vehicle_id = input("Enter Vehicle ID: ")
    days = int(input("Enter Number of Rental Days: "))

    # Check if customer exists
    cursor.execute("SELECT * FROM Customers WHERE customer_id=?", (customer_id,))
    customer = cursor.fetchone()

    if customer is None:
        print("\nCustomer ID not found.")
        connection.close()
        return

    # Check vehicle
    cursor.execute("SELECT price_per_day, status FROM Vehicles WHERE vehicle_id=?", (vehicle_id,))
    vehicle = cursor.fetchone()

    if vehicle is None:
        print("\nVehicle ID not found.")
        connection.close()
        return

    if vehicle[1] != "Available":
        print("\nVehicle is already rented.")
        connection.close()
        return

    price_per_day = vehicle[0]
    total_amount = price_per_day * days

    rental_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    INSERT INTO Rentals
    (customer_id, vehicle_id, rental_date, return_date, days_rented, total_amount)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (customer_id, vehicle_id, rental_date, None, days, total_amount))

    cursor.execute("""
    UPDATE Vehicles
    SET status='Rented'
    WHERE vehicle_id=?
    """, (vehicle_id,))

    connection.commit()
    connection.close()

    print("\nVehicle Rented Successfully!")
    print(f"Total Amount: ₹{total_amount}")

# ==========================
# RETURN VEHICLE
# ==========================

def return_vehicle():

    connection = get_connection()
    cursor = connection.cursor()

    vehicle_id = input("Enter Vehicle ID to Return: ")

    cursor.execute("""
    SELECT * FROM Rentals
    WHERE vehicle_id=? AND return_date IS NULL
    """, (vehicle_id,))

    rental = cursor.fetchone()

    if rental is None:
        print("\nNo active rental found for this vehicle.")
        connection.close()
        return

    return_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    UPDATE Rentals
    SET return_date=?
    WHERE rental_id=?
    """, (return_date, rental[0]))

    cursor.execute("""
    UPDATE Vehicles
    SET status='Available'
    WHERE vehicle_id=?
    """, (vehicle_id,))

    connection.commit()
    connection.close()

    print("\nVehicle Returned Successfully!")

# ==========================
# RENTAL HISTORY
# ==========================

def rental_history():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        Rentals.rental_id,
        Customers.customer_name,
        Vehicles.vehicle_name,
        Rentals.rental_date,
        Rentals.return_date,
        Rentals.days_rented,
        Rentals.total_amount
    FROM Rentals
    JOIN Customers
        ON Rentals.customer_id = Customers.customer_id
    JOIN Vehicles
        ON Rentals.vehicle_id = Vehicles.vehicle_id
    """)

    rentals = cursor.fetchall()

    if len(rentals) == 0:
        print("\nNo Rental History Found.")

    else:

        print("\n======================== RENTAL HISTORY ========================\n")

        print("=" * 110)
        print(f"{'ID':<5}{'Customer':<20}{'Vehicle':<15}{'Rent Date':<15}{'Return Date':<15}{'Days':<8}{'Amount'}")
        print("=" * 110)

        for rental in rentals:
            print(
                f"{rental[0]:<5}"
                f"{rental[1]:<20}"
                f"{rental[2]:<15}"
                f"{str(rental[3]):<15}"
                f"{str(rental[4]):<15}"
                f"{rental[5]:<8}"
                f"₹{rental[6]:.2f}"
            )

        print("=" * 110)

    connection.close()
# ==========================
# UPDATE VEHICLE
# ==========================

def update_vehicle():

    connection = get_connection()
    cursor = connection.cursor()

    vehicle_id = get_integer("Enter Vehicle ID to Update: ")

    cursor.execute("SELECT * FROM Vehicles WHERE vehicle_id=?", (vehicle_id,))
    vehicle = cursor.fetchone()

    if vehicle is None:
        print("\nVehicle not found.")
        connection.close()
        return

    print("\nLeave blank to keep the current value.\n")

    vehicle_name = input(f"Vehicle Name ({vehicle[1]}): ").strip()
    vehicle_type = input(f"Vehicle Type ({vehicle[2]}): ").strip()
    brand = input(f"Brand ({vehicle[3]}): ").strip()
    price = input(f"Price Per Day ({vehicle[4]}): ").strip()

    if vehicle_name == "":
        vehicle_name = vehicle[1]

    if vehicle_type == "":
        vehicle_type = vehicle[2]

    if brand == "":
        brand = vehicle[3]

    if price == "":
        price = vehicle[4]
    else:
        try:
            price = float(price)
            if price <= 0:
                print("\nPrice must be greater than 0.")
                connection.close()
                return
        except ValueError:
            print("\nInvalid price.")
            connection.close()
            return

    try:
        cursor.execute("""
        UPDATE Vehicles
        SET vehicle_name=?,
            vehicle_type=?,
            brand=?,
            price_per_day=?
        WHERE vehicle_id=?
        """, (vehicle_name, vehicle_type, brand, price, vehicle_id))

        connection.commit()

        print("\nVehicle Updated Successfully!")

    except sqlite3.Error as e:
        print(f"\nDatabase Error: {e}")

    finally:
        connection.close()

# ==========================
# DELETE VEHICLE
# ==========================

def delete_vehicle():

    connection = get_connection()
    cursor = connection.cursor()

    vehicle_id = input("Enter Vehicle ID to Delete: ").strip()

    cursor.execute("SELECT * FROM Vehicles WHERE vehicle_id=?", (vehicle_id,))
    vehicle = cursor.fetchone()

    if vehicle is None:
        print("\nVehicle not found.")
        connection.close()
        return

    print("\n========== VEHICLE DETAILS ==========\n")
    print(f"Vehicle ID      : {vehicle[0]}")
    print(f"Vehicle Name    : {vehicle[1]}")
    print(f"Vehicle Type    : {vehicle[2]}")
    print(f"Brand           : {vehicle[3]}")
    print(f"Price Per Day   : ₹{vehicle[4]}")
    print(f"Status          : {vehicle[5]}")

    confirm = input("\nDelete this vehicle? (Y/N): ").upper()

    if confirm != "Y":
        print("\nDeletion Cancelled.")
        connection.close()
        return

    try:
        cursor.execute("DELETE FROM Vehicles WHERE vehicle_id=?", (vehicle_id,))
        connection.commit()
        print("\nVehicle Deleted Successfully!")

    except sqlite3.IntegrityError:
        print("\nCannot delete this vehicle because it has rental records.")

    connection.close()

# ==========================
# UPDATE CUSTOMER
# ==========================

def update_customer():

    connection = get_connection()
    cursor = connection.cursor()

    customer_id = get_integer("Enter Customer ID to Update: ")

    cursor.execute("SELECT * FROM Customers WHERE customer_id=?", (customer_id,))
    customer = cursor.fetchone()

    if customer is None:
        print("\nCustomer not found.")
        connection.close()
        return

    print("\nLeave blank to keep the current value.\n")

    name = input(f"Customer Name ({customer[1]}): ").strip()
    phone = input(f"Phone Number ({customer[2]}): ").strip()
    email = input(f"Email ({customer[3]}): ").strip()
    license_no = input(f"Driving License ({customer[4]}): ").strip()

    if name == "":
        name = customer[1]

    if phone == "":
        phone = customer[2]
    else:
        if not phone.isdigit() or len(phone) != 10:
            print("\nPhone number must contain exactly 10 digits.")
            connection.close()
            return

    if email == "":
        email = customer[3]

    if license_no == "":
        license_no = customer[4]

    try:

        cursor.execute("""
        UPDATE Customers
        SET customer_name=?,
            phone_number=?,
            email=?,
            driving_license=?
        WHERE customer_id=?
        """, (name, phone, email, license_no, customer_id))

        connection.commit()

        print("\nCustomer Updated Successfully!")

    except sqlite3.Error as e:
        print(f"\nDatabase Error: {e}")

    finally:
        connection.close()

# ==========================
# DELETE CUSTOMER
# ==========================

def delete_customer():

    connection = get_connection()
    cursor = connection.cursor()

    customer_id = input("Enter Customer ID to Delete: ").strip()

    cursor.execute("SELECT * FROM Customers WHERE customer_id=?", (customer_id,))
    customer = cursor.fetchone()

    if customer is None:
        print("\nCustomer not found.")
        connection.close()
        return

    print("\n========== CUSTOMER DETAILS ==========\n")
    print(f"Customer ID      : {customer[0]}")
    print(f"Customer Name    : {customer[1]}")
    print(f"Phone Number     : {customer[2]}")
    print(f"Email            : {customer[3]}")
    print(f"Driving License  : {customer[4]}")

    confirm = input("\nDelete this customer? (Y/N): ").upper()

    if confirm != "Y":
        print("\nDeletion Cancelled.")
        connection.close()
        return

    try:
        cursor.execute("DELETE FROM Customers WHERE customer_id=?", (customer_id,))
        connection.commit()
        print("\nCustomer Deleted Successfully!")

    except sqlite3.IntegrityError:
        print("\nCannot delete this customer because rental records exist.")

    connection.close()


# ==========================
# GENERATE BILL
# ==========================

def generate_bill():

    connection = get_connection()
    cursor = connection.cursor()

    rental_id = input("Enter Rental ID: ")

    cursor.execute("""
    SELECT
        Rentals.rental_id,
        Customers.customer_name,
        Customers.phone_number,
        Vehicles.vehicle_name,
        Vehicles.brand,
        Rentals.rental_date,
        Rentals.return_date,
        Rentals.days_rented,
        Rentals.total_amount
    FROM Rentals
    JOIN Customers
        ON Rentals.customer_id = Customers.customer_id
    JOIN Vehicles
        ON Rentals.vehicle_id = Vehicles.vehicle_id
    WHERE Rentals.rental_id = ?
    """, (rental_id,))

    bill = cursor.fetchone()

    if bill is None:
        print("\nRental Record Not Found.")
        connection.close()
        return

    print("\n" + "=" * 45)
    print("          VEHICLE RENTAL BILL")
    print("=" * 45)
    print(f"Rental ID       : {bill[0]}")
    print(f"Customer Name   : {bill[1]}")
    print(f"Phone Number    : {bill[2]}")
    print(f"Vehicle         : {bill[3]}")
    print(f"Brand           : {bill[4]}")
    print(f"Rental Date     : {bill[5]}")
    print(f"Return Date     : {bill[6]}")
    print(f"Days Rented     : {bill[7]}")
    print(f"Total Amount    : ₹{bill[8]}")
    print("=" * 45)

    connection.close()

# ===================================
# DASHBOARD
# ===================================

def dashboard():

    connection = get_connection()
    cursor = connection.cursor()

    # Total Vehicles
    cursor.execute("SELECT COUNT(*) FROM Vehicles")
    total_vehicles = cursor.fetchone()[0]

    # Total Customers
    cursor.execute("SELECT COUNT(*) FROM Customers")
    total_customers = cursor.fetchone()[0]

    # Total Rentals
    cursor.execute("SELECT COUNT(*) FROM Rentals")
    total_rentals = cursor.fetchone()[0]

    # Available Vehicles
    cursor.execute("SELECT COUNT(*) FROM Vehicles WHERE status='Available'")
    available = cursor.fetchone()[0]

    # Rented Vehicles
    cursor.execute("SELECT COUNT(*) FROM Vehicles WHERE status='Rented'")
    rented = cursor.fetchone()[0]

    # Total Revenue
    cursor.execute("SELECT IFNULL(SUM(total_amount),0) FROM Rentals")
    revenue = cursor.fetchone()[0]

    connection.close()

    print("=" * 55)
    print("        VEHICLE RENTAL SYSTEM DASHBOARD")
    print("=" * 55)
    print(f" Total Vehicles     : {total_vehicles}")
    print(f" Total Customers    : {total_customers}")
    print(f" Total Rentals      : {total_rentals}")
    print(f" Available Vehicles : {available}")
    print(f" Rented Vehicles    : {rented}")
    print(f" Total Revenue      : ₹{revenue:.2f}")
    print("=" * 55)


def get_dashboard_data():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Vehicles")
    total_vehicles = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Customers")
    total_customers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Rentals")
    total_rentals = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Vehicles WHERE status='Available'"
    )
    available = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Vehicles WHERE status='Rented'"
    )
    rented = cursor.fetchone()[0]

    cursor.execute(
        "SELECT IFNULL(SUM(total_amount),0) FROM Rentals"
    )
    revenue = cursor.fetchone()[0]

    connection.close()

    return {
        "vehicles": total_vehicles,
        "customers": total_customers,
        "rentals": total_rentals,
        "available": available,
        "rented": rented,
        "revenue": revenue
    }
if __name__ == "__main__":
    menu()