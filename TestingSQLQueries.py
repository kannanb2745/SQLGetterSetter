from SQLGetterSetter import MainClass

detail = {
    'host': 'localhost',
    'user': 'kannan',
    'password': 'Kannan123!',
    'database': 'SalesManagement'
}
obj = MainClass(connection_params = detail)




# --------------------------------------------------------------------------------------------------------------------------------------
def show(r):
    try:
        for i in r:
            print(i)
    except Exception as e:
        print(e)
    finally:
        print('-----------------------------------\n')
        print('-----------------------------------\n')
        
        
        
        
# Table Management
# SQL CREATE TABLE
# CREATE TABLE Customers (
#     CustomerID INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(50) NOT NULL,
#     Email VARCHAR(50) UNIQUE,
#     City VARCHAR(50),
#     Country VARCHAR(50),
#     Phone VARCHAR(15)
# );
obj.create_table('Customers', 'CustomerID INT AUTO_INCREMENT PRIMARY KEY','Name VARCHAR(50) NOT NULL, Email VARCHAR(50) UNIQUE','City VARCHAR(50)','Country VARCHAR(50)','Phone VARCHAR(15)').exe()


# CREATE TABLE Employees (
#     EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(50) NOT NULL,
#     Position VARCHAR(50),
#     HireDate DATE,
#     Salary DECIMAL(10, 2)
# );
obj.create_table('Employees', 'EmployeeID INT AUTO_INCREMENT PRIMARY KEY','Name VARCHAR(50) NOT NULL, Position VARCHAR(50)','HireDate DATE','Salary DECIMAL(10, 2)').exe()


# CREATE TABLE Products (
#     ProductID INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(50) NOT NULL,
#     Category VARCHAR(50),
#     Price DECIMAL(10, 2),
#     Stock INT,
#     CreatedDate DATE DEFAULT '2024-01-01' -- Replace with a fixed default date
# );
obj.create_table('Products', 'ProductID INT AUTO_INCREMENT PRIMARY KEY','Name VARCHAR(50) NOT NULL','Category VARCHAR(50)','Price DECIMAL(10, 2)','Stock INT',"CreatedDate DATE DEFAULT '2024-01-01'").exe()

# CREATE TABLE Orders (
#     OrderID INT AUTO_INCREMENT PRIMARY KEY,
#     CustomerID INT,
#     EmployeeID INT,
#     OrderDate DATE,
#     TotalAmount DECIMAL(10, 2),
#     FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
#     FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
# );
obj.create_table('Orders', 'OrderID INT AUTO_INCREMENT PRIMARY KEY','CustomerID INT','EmployeeID INT','OrderDate DATE','TotalAmount DECIMAL(10, 2)','FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)','FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)').exe()


# CREATE TABLE OrderDetails (
#     OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
#     OrderID INT,
#     ProductID INT,
#     Quantity INT,
#     Price DECIMAL(10, 2),
#     FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
#     FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
# );
obj.create_table('OrderDetails', 'OrderDetailID INT AUTO_INCREMENT PRIMARY KEY','OrderID INT','ProductID INT','Quantity INT','Price DECIMAL(10, 2)','FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)','FOREIGN KEY (ProductID) REFERENCES Products(ProductID)').exe()


# -- Insert Customers
# INSERT INTO Customers (Name, Email, City, Country, Phone)
# VALUES 
# [
# ('John Doe', 'john.doe@example.com', 'New York', 'USA', '1234567890'),
# ('Jane Smith', 'jane.smith@example.com', 'London', 'UK', '0987654321'),
# ('Ahmed Ali', 'ahmed.ali@example.com', 'Cairo', 'Egypt', '1122334455')]
obj.insert('Customers', [('John Doe', 'john.doe@example.com', 'New York', 'USA', '1234567890'),
('Jane Smith', 'jane.smith@example.com', 'London', 'UK', '0987654321'),
('Ahmed Ali', 'ahmed.ali@example.com', 'Cairo', 'Egypt', '1122334455')],columns = ['Name', 'Email', 'City', 'Country', 'Phone']).exe()



# -- Insert Employees
# INSERT INTO Employees (Name, Position, HireDate, Salary)
# VALUES 
# ('Alice Johnson', 'Manager', '2020-01-15', 75000),
# ('Bob Brown', 'Sales Executive', '2021-07-10', 50000),
# ('Charlie Davis', 'Clerk', '2019-05-20', 35000);
obj.insert('Employees', [('Alice Johnson', 'Manager', '2020-01-15', 75000),
('Bob Brown', 'Sales Executive', '2021-07-10', 50000),
('Charlie Davis', 'Clerk', '2019-05-20', 35000)],columns = ['Name', 'Position', 'HireDate', 'Salary']).exe()



# -- Insert Products
# INSERT INTO Products (Name, Category, Price, Stock)
# VALUES 
# ('Laptop', 'Electronics', 1000, 50),
# ('Smartphone', 'Electronics', 800, 100),
# ('Tablet', 'Electronics', 600, 30),
# ('Desk Chair', 'Furniture', 150, 20);
obj.insert('Products', [('Laptop', 'Electronics', 1000, 50),
('Smartphone', 'Electronics', 800, 100),
('Tablet', 'Electronics', 600, 30),
('Desk Chair', 'Furniture', 150, 20)],columns = ['Name', 'Category', 'Price', 'Stock']).exe()



# -- Insert Orders
# INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, TotalAmount)
# VALUES 
# (1, 2, '2024-01-15', 1800),
# (2, 1, '2024-01-20', 1000),
# (3, 3, '2024-01-25', 600);
obj.insert('Orders', [(1, 2, '2024-01-15', 1800),
(2, 1, '2024-01-20', 1000),
(3, 3, '2024-01-25', 600)],columns = ['CustomerID', 'EmployeeID', 'OrderDate', 'TotalAmount']).exe()


# -- Insert OrderDetails
# INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price)
# VALUES 
# (1, 1, 1, 1000),
# (1, 2, 1, 800),
# (2, 4, 2, 300),
# (3, 3, 1, 600);
obj.insert('OrderDetails', [(1, 1, 1, 1000),(1, 2, 1, 800),(2, 4, 2, 300),(3, 3, 1, 600)],columns = ['OrderID', 'ProductID', 'Quantity', 'Price']).exe()


# Basic Operations
# SQL SELECT
# SELECT * FROM Customers;
show(obj.select().table('Customers').exe())

# SQL DISTINCT=
# SELECT DISTINCT City FROM Customers;
show(obj.select(' ').distinct('City').table('Customers').exe())

# SQL WHERE
# SELECT * FROM Products WHERE Stock > 30;
show(obj.select().table('Products').where('Stock > 30').exe())
 
# SQL ORDER BY
# SELECT * FROM Employees ORDER BY Salary DESC;
show(obj.select().table('Employees').orderby(('Salary','DESC')).exe())

# SQL LIMIT / FETCH
# SELECT * FROM Products LIMIT 2;
show(obj.select().table('Products').limit(2).exe())

# SQL SELECT TOP (Alternative for MySQL)
# SELECT * FROM Employees LIMIT 3;
show(obj.select().table('Employees').limit(3).exe())

# Operators and Clauses
# SQL Comparison Operators
# SELECT * FROM Orders WHERE TotalAmount >= 1000;
show(obj.select().table('Orders').where('TotalAmount >= 1000').exe())

# SQL Logical Operators (AND / OR)
# SELECT * FROM Customers WHERE Country = 'USA' AND City = 'New York';
show(obj.select().table('Customers').where("Country = 'USA'","City = 'New York'", operator='AND').exe())
 
# SQL NOT
# SELECT * FROM Employees WHERE NOT Position = 'Manager';
show(obj.select().table('Employees').where("NOT Position = 'Manager'").exe())

# SQL LIKE
# SELECT * FROM Customers WHERE Name LIKE 'J%';
show(obj.select().table('Customers').where("Name LIKE 'J%'").exe())

# SQL IN
# SELECT * FROM Customers WHERE Country IN ('USA', 'UK');
show(obj.select().table('Customers').where("Country").IN('USA', 'UK').exe())

# SQL BETWEEN
# SELECT * FROM Products WHERE Price BETWEEN 100 AND 900;
show(obj.select().table('Products').where("Price").between(100, 900).exe())

# SQL IS NULL
# SELECT * FROM Products WHERE Stock IS NULL;
show(obj.select().table('Products').where("Stock").isnull().exe())

# Data Manipulation Language (DML)
# SQL INSERT
# INSERT INTO Products (Name, Category, Price, Stock) 
# VALUES ('Monitor', 'Electronics', 200, 25);
obj.insert('Products', [('Monitor', 'Electronics', 200, 25)],columns = ['Name', 'Category', 'Price', 'Stock']).exe()

# SQL INSERT INTO SELECT
# INSERT INTO Employees (Name, Position, HireDate, Salary) 
# SELECT Name, 'Intern', CURRENT_DATE, 30000 FROM Customers WHERE Country = 'USA';
# insert_into_select(self, source, destination, source_columns=None, destination_columns=None):
obj.insert_into_select(source='Customers', destination='Employees', source_columns=['Name', "'Intern'","CURRENT_DATE",'30000'], destination_columns=['Name', 'Position', 'HireDate', 'Salary']).where("Country = 'USA'").exe()

# SQL UPDATE
# UPDATE Products SET CreatedDate = '2024-01-03' WHERE ProductID = 1;
# :param changes: List of tuples containing column name and new value (e.g., [('column1', 'value1'), ('column2', 'value2')]).
obj.update('Products', changes=[('CreatedDate', '2024-01-03')]).where('ProductID = 1').exe()

# SQL DELETE
# DELETE FROM Products WHERE ProductID = 7;
obj.delete('Products').where('ProductID = 7').exe()

# Subqueries
# SQL Subquery
# SELECT * FROM Products WHERE Price > (SELECT AVG(Price) FROM Products);
show(obj.select().table('Products').where('Price >').sub_select(' ').avg('Price').table('Products').exe())

# SQL Correlated Subquery 
# SELECT Name, Stock FROM Products P 
# WHERE Stock > (SELECT AVG(Stock) FROM Products WHERE Category = P.Category);
show(obj.select('Name, Stock').table('Products P').where('Stock >').sub_select(' ').avg('Stock').table('Products').where('Category = P.Category').exe())

# SQL EXISTS
# SELECT * FROM Customers WHERE EXISTS 
# (SELECT 1 FROM Orders WHERE Orders.CustomerID = Customers.CustomerID);
show(obj.select().table('Customers').where('EXISTS').sub_select('1').table('Orders').where('Orders.CustomerID = Customers.CustomerID').exe())

# SQL ALL / ANY
# SELECT * FROM Employees WHERE Salary > ALL 
# (SELECT Salary FROM Employees WHERE Position = 'Clerk');
show(obj.select().table('Employees').where('Salary > ALL').sub_select('Salary').table('Employees').where("Position = 'Clerk'").exe())

# Null and Null Functions
# SQL NULL Values
# SELECT * FROM Products WHERE Stock IS NOT NULL;
show(obj.select().table('Products').where('Stock').isnotnull().exe())

# SQL Null Functions
# SELECT COALESCE(Stock, 0) AS AvailableStock FROM Products;
show(obj.select(' ').coalesce('Stock', 0).AS('AvailableStock').table('Products').exe())

# Database Management
# SQL CREATE DB 
# CREATE DATABASE SalesManagement;
obj.create_db('SalesManagementBackup').exe()

# SQL DROP DB
# DROP DATABASE SalesManagement;
obj.drop_db('SalesManagementBackup').exe()


# CREATE TABLE BackupCustomers AS SELECT * FROM Customers;
# SQL ALTER TABLE
# Add Column
obj.add_column('Customers', 'New_Column VARCHAR(50)').exe()


# ALTER TABLE Customers ADD Gender VARCHAR(10);
# Drop Column
obj.drop_column('Customers', 'New_Column').exe()
 
 
# CREATE INDEX idx_ProductName ON Products (Name);
# SQL Views
obj.create_index('Products', 'Name').exe() 

# CREATE VIEW HighValueOrders AS 
# SELECT * FROM Orders WHERE TotalAmount > 1000;
show(obj.select().table('Orders').where('TotalAmount > 1000').exe())

# SQL Aggregate Functions
# SQL AVG
# SELECT AVG(Price) AS AveragePrice FROM Products;
show(obj.select(' ').avg('Price').AS('AveragePrice').table('Products').exe())


# SQL COUNT
# SELECT COUNT(*) AS TotalOrders FROM Orders;
show(obj.select(' ').count('*').AS('TotalOrders').table('Orders').exe())

# SQL MAX
# SELECT MAX(Salary) AS HighestSalary FROM Employees;
show(obj.select(' ').max('Salary').AS('HighestSalary').table('Employees').exe())

# SQL MIN TotalAmouPricent
# SELECT MIN(Salary) AS LowestSalary FROM Employees;
show(obj.select(' ').min('Salary').AS('LowestSalary').table('Employees').exe())

# SQL SUM
# SELECT SUM(Quantity) AS TotalItemsSold FROM OrderDetails;
show(obj.select(' ').sum('Quantity').AS('TotalItemsSold').table('OrderDetails').exe())

# Date and Time
# SELECT * FROM Orders WHERE OrderDate > '2024-01-01';
show(obj.select().table('Orders').where("OrderDate > '2024-01-01'").exe())

# Stored Procedures
# DELIMITER //
# CREATE PROCEDURE GetCustomerOrders (IN custID INT)
# BEGIN
    # SELECT * FROM Orders WHERE CustomerID = custID;
# END //
# DELIMITER ;
obj.create_procedure('GetCustomerOrders', ["SELECT * FROM Orders WHERE CustomerID = custID;"], params=["IN custID INT"]).exe()

# CALL GetCustomerOrders(1);
show(obj.call_procedure('GetCustomerOrders', [1]))

