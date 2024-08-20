CREATE DATABASE DA_iTee;
GO

USE DA_iTee;
GO

/* Scripts to Create Tables */

-- Customer Dimension Table
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    Customer_Address VARCHAR(255),
    PhoneNumber VARCHAR(20)
);

-- Vehicle Dimension Table 
CREATE TABLE Vehicle (
    VehicleID INT PRIMARY KEY,
    Make VARCHAR(50),
    Model VARCHAR(50),
    VehicleYear INT,
    Color VARCHAR(20),
    VIN VARCHAR(50),
    RegistrationNumber VARCHAR(50),
    Mileage INT
);

-- Create Invoice Fact Table 
CREATE TABLE InvoiceFact (
    Invoice_Number VARCHAR(50) PRIMARY KEY,
    InvoiceDate DATE,
    CustomerID INT,
    VehicleID INT,
    SubtotalAmount DECIMAL(10, 2),
    SalesTaxRate DECIMAL(5, 2),
    SalesTaxAmount DECIMAL(10, 2),
    TotalAmount DECIMAL(10, 2),
    Total_Labour DECIMAL(10, 2),
    Total_Parts DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);

-- Create Service Performed Dimension Table
CREATE TABLE ServicePerformed (
    ServiceID INT PRIMARY KEY,
	Invoice_Number VARCHAR(50),
    ServiceDescription VARCHAR(255),
    Hours DECIMAL(5, 2),
    Rate DECIMAL(10, 2),
    Amount DECIMAL(10, 2),
    FOREIGN KEY (Invoice_Number) REFERENCES InvoiceFact(Invoice_Number)
);

-- Part Dimension Table
CREATE TABLE Part (
    PartID INT PRIMARY KEY,
    PartNumber VARCHAR(50),
    PartName VARCHAR(255),
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    Amount DECIMAL(10, 2),
	Invoice_Number VARCHAR(50),
	FOREIGN KEY (Invoice_Number) REFERENCES InvoiceFact(Invoice_Number)
);
