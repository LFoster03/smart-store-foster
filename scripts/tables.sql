CREATE TABLE IF NOT EXISTS customers (
    CustomerID INTEGER PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Region VARCHAR NOT NULL,
    JoinDate DATE,
    LoyaltyPoints INTEGER,
    CustomerSegment VARCHAR,
    LastPurchaseDate DATE
);

CREATE TABLE IF NOT EXISTS products (
    ProductID INTEGER PRIMARY KEY,
    ProductName VARCHAR NOT NULL,
    Category VARCHAR NOT NULL,
    UnitPrice DECIMAL NOT NULL,
    StockQuantity INTEGER NOT NULL,
    Supplier VARCHAR,
    AverageRating DECIMAL
);

CREATE TABLE IF NOT EXISTS sales (
    TransactionID INTEGER PRIMARY KEY,
    SaleDate DATE,
    CustomerID INTEGER,
    ProductID INTEGER,
    StoreID INTEGER,
    CampaignID INTEGER,
    SaleAmount DECIMAL NOT NULL,
    DiscountPercent DECIMAL,
    PaymentType VARCHAR,
    FOREIGN KEY (CustomerID) REFERENCES customers (CustomerID),
    FOREIGN KEY (ProductID) REFERENCES products (ProductID)
);

