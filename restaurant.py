# Importing MySQL connector module
import mysql.connector as my

# Establishing connection with MySQL database
con = my.connect(
    host="localhost",
    user="root",
    password="YourPassword",#write your password here
    database="Restaurant"
)

# Creating cursor object to execute SQL queries
cur = con.cursor()

# Function to add new bill details
def Insert_Data():
    print("\n--- ADD NEW BILL DETAILS ---")
    billno = int(input("Enter Bill Number: "))
    cname = input("Enter Customer Name: ")
    tno = int(input("Enter Table Number: "))
    item = input("Enter Item Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Item: "))
    total = qty * price
    query = "INSERT INTO Bills VALUES({}, '{}', {}, '{}', {}, {}, {}, CURDATE())".format(
        billno, cname, tno, item, qty, price, total)
    cur.execute(query)
    con.commit()
    print("Bill added successfully!")
    Homepage()

# Function to delete a bill using Bill Number
def Delete_Data():
    print("\n--- DELETE BILL DETAILS ---")
    x = int(input("Enter the Bill Number to delete: "))
    query = "DELETE FROM Bills WHERE Bill_No={}".format(x)
    cur.execute(query)
    con.commit()
    print("Bill deleted successfully!")
    Homepage()

# Function to update bill details
def Update_Data():
    print("\n--- UPDATE BILL DETAILS ---")
    bill = int(input("Enter Bill Number to update: "))
    new_qty = int(input("Enter new Quantity: "))
    new_price = float(input("Enter new Price per Item: "))
    new_total = new_qty * new_price
    query = "UPDATE Bills SET Quantity={}, Price_Per_Item={}, Total_Amount={} WHERE Bill_No={}".format(
        new_qty, new_price, new_total, bill)
    cur.execute(query)
    con.commit()
    print("Bill updated successfully!")
    Homepage()

# Function to search a bill by Bill Number
def Search_Data():
    print("\n--- SEARCH BILL DETAILS ---")
    bill = int(input("Enter Bill Number to search: "))
    query = "SELECT * FROM Bills WHERE Bill_No={}".format(bill)
    cur.execute(query)
    data = cur.fetchall()
    if data:
        print("\nBill Details:")
        print("Bill_No | Customer_Name | Table_No | Item_Name | Quantity | Price_Per_Item | Total_Amount | Order_Date")
        for row in data:
            print(row)
    else:
        print("No record found with Bill No:", bill)
    Homepage()

# Function to display all bill records
def Display_All():
    print("\n--- ALL BILL RECORDS ---")
    cur.execute("SELECT * FROM Bills")
    data = cur.fetchall()
    if data:
        print("Bill_No | Customer_Name | Table_No | Item_Name | Quantity | Price_Per_Item | Total_Amount | Order_Date")
        for row in data:
            print(row)
    else:
        print("No bills found.")
    Homepage()

# Main menu function
def Homepage():
    print("\n========= RESTAURANT BILLING SYSTEM =========")
    print("1. Add New Bill")
    print("2. Delete Bill")
    print("3. Update Bill")
    print("4. Search Bill")
    print("5. Display All Bills")
    print("6. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        Insert_Data()
    elif ch == 2:
        Delete_Data()
    elif ch == 3:
        Update_Data()
    elif ch == 4:
        Search_Data()
    elif ch == 5:
        Display_All()
    elif ch == 6:
        print("Exiting... Thank you!")
        exit()
    else:
        print("Invalid choice! Try again.")
        Homepage()

Homepage()
