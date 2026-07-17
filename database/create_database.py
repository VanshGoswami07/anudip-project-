import sqlite3

# Connect to the database
connection = sqlite3.connect("database/vehicle_rental.db")

# Create a cursor
cursor = connection.cursor()

# Create Vehicles table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Vehicles(
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_name TEXT NOT NULL,
    vehicle_type TEXT NOT NULL,
    brand TEXT NOT NULL,
    price_per_day REAL NOT NULL,
    status TEXT NOT NULL
)
""")
# Create Customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT,
    driving_license TEXT NOT NULL
)
""")
# Save changes
connection.commit()

print("Vehicles and Customers tables created successfully!")

# Close database
connection.close()