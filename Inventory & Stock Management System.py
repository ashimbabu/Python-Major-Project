import sqlite3


# Database Connection

class Database:
    def __init__(self, db_name="inventory.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER,
            price REAL
        )
        """)
        self.conn.commit()

    def close(self):
        self.conn.close()



# Inventory Management

class Inventory:
    def __init__(self, database):
        self.db = database

    def add_product(self, name, category, quantity, price):
        self.db.cursor.execute("""
        INSERT INTO inventory (name, category, quantity, price)
        VALUES (?, ?, ?, ?)
        """, (name, category, quantity, price))
        self.db.conn.commit()
        print("Product added successfully.")

    def view_products(self):
        self.db.cursor.execute("SELECT * FROM inventory")
        products = self.db.cursor.fetchall()
        print("\nID | Name | Category | Quantity | Price")
        print("-" * 50)
        for p in products:
            print(p)

    def update_stock(self, product_id, quantity):
        self.db.cursor.execute("""
        UPDATE inventory SET quantity = quantity + ?
        WHERE id = ?
        """, (quantity, product_id))
        self.db.conn.commit()
        print("Stock updated successfully.")

    def remove_product(self, product_id):
        self.db.cursor.execute("DELETE FROM inventory WHERE id = ?", (product_id,))
        self.db.conn.commit()
        print("Product removed successfully.")

    def low_stock_alert(self, threshold=5):
        self.db.cursor.execute("""
        SELECT name, quantity FROM inventory WHERE quantity <= ?
        """, (threshold,))
        items = self.db.cursor.fetchall()
        if items:
            print("\nLow Stock Alert:")
            for item in items:
                print(f"{item[0]} - Quantity: {item[1]}")
        else:
            print("\nNo low-stock items.")



# Menu Driven System

def menu():
    print("""
Inventory & Stock Management System
-----------------------------------
1. Add Product
2. View Products
3. Stock In / Stock Out
4. Delete Product
5. Low Stock Alert
6. Exit
""")


def main():
    db = Database()
    inventory = Inventory(db)

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Product Name: ")
            category = input("Category: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            inventory.add_product(name, category, quantity, price)

        elif choice == "2":
            inventory.view_products()

        elif choice == "3":
            product_id = int(input("Product ID: "))
            quantity = int(input("Enter quantity (+ for IN, - for OUT): "))
            inventory.update_stock(product_id, quantity)

        elif choice == "4":
            product_id = int(input("Product ID to delete: "))
            inventory.remove_product(product_id)

        elif choice == "5":
            inventory.low_stock_alert()

        elif choice == "6":
            db.close()
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()