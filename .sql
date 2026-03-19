--SQL commands to create the database restaurant and the Bills table
CREATE DATABASE Restaurant;
USE Restaurant;
CREATE TABLE Bills (
    Bill_No INT PRIMARY KEY,
    Customer_Name VARCHAR(50),
    Table_No INT,
    Item_Name VARCHAR(50),
    Quantity INT,
    Price_Per_Item DECIMAL(8,2),
    Total_Amount DECIMAL(10,2),
    Order_Date DATE
);
