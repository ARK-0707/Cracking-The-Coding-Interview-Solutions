
# Building Database

Questions 1 through 3 refer to the database schema and queries below. Each apartment can have multiple tenants, and each tenant can have multiple apartments. Each apartment belongs to one building and each building belongs to one complex.

---

## Database Schema

### Tables

#### Database Structure:

- **Complexes Table**:
    - `ComplexID`: A unique identifier for each complex.
    - `ComplexName`: Name of the complex.

- **Buildings Table**:
    - `BuildingID`: A unique identifier for each building.
    - `ComplexID`: A foreign key linking the building to a complex.
    - `BuildingName`: Name of the building.
    - `Address`: Address of the building.

- **Apartments Table**:
    - `AptID`: A unique identifier for each apartment.
    - `UnitNumber`: Unit number of the apartment.
    - `BuildingID`: Foreign key linking the apartment to a building.

- **Tenants Table**:
    - `TenantID`: A unique identifier for each tenant.
    - `TenantName`: Name of the tenant.

- **AptTenants Table**:
    - `TenantID`: Foreign key linking the tenant to an apartment.
    - `AptID`: Foreign key linking the apartment to a tenant.

- **Requests Table**:
    - `RequestID`: A unique identifier for each request.
    - `Status`: Status of the request (e.g., Pending, Resolved, etc.).
    - `AptID`: Foreign key linking the request to an apartment.
    - `Description`: Description of the request.

---

## Data and Relationship Diagram

The relationships between the tables are as follows:

1. **Complexes to Buildings**: One-to-many (A complex can have multiple buildings).
2. **Buildings to Apartments**: One-to-many (A building can have multiple apartments).
3. **Apartments to Tenants**: Many-to-many (An apartment can have multiple tenants and vice versa).
4. **Apartments to Requests**: One-to-many (An apartment can have multiple requests).

The diagram below visually represents these relationships:

```plaintext
+-------------------+     +---------------------+     +---------------------+
|    Complexes     |     |     Buildings       |     |    Apartments       |
+-------------------+     +---------------------+     +---------------------+
| ComplexID (PK)    |<--- | BuildingID (PK)     |<--- | AptID (PK)          |
| ComplexName       |     | ComplexID (FK)      |     | UnitNumber          |
+-------------------+     | BuildingName        |     | BuildingID (FK)     |
                          | Address             |     +---------------------+
                          +---------------------+     | AptID (FK)          |
                                                     +---------------------+
                                                            |
                                                           |
                                             +--------------------------+
                                             |        Tenants           |
                                             +--------------------------+
                                             | TenantID (PK)            |
                                             | TenantName               |
                                             +--------------------------+
                                                     |
                                          +---------------------+
                                          |    AptTenants       |
                                          +---------------------+
                                          | TenantID (FK)       |
                                          | AptID (FK)          |
                                          +---------------------+
                                                     |
                                          +---------------------+
                                          |     Requests        |
                                          +---------------------+
                                          | RequestID (PK)      |
                                          | Status              |
                                          | AptID (FK)          |
                                          | Description         |
                                          +---------------------+
```

---

## Data Insertions

### Initial Data

#### Insert Data into `Complexes`
```sql
INSERT INTO Complexes (ComplexID, ComplexName)
VALUES 
(1, 'Greenwood Complex'),
(2, 'Lakeside Residences');
```

#### Insert Data into `Buildings`
```sql
INSERT INTO Buildings (BuildingID, ComplexID, BuildingName, Address)
VALUES 
(1, 1, 'Greenwood Tower 1', '123 Main St'),
(2, 1, 'Greenwood Tower 2', '124 Main St'),
(3, 2, 'Lakeside Tower', '456 Lake Rd');
```

#### Insert Data into `Apartments`
```sql
INSERT INTO Apartments (AptID, UnitNumber, BuildingID)
VALUES 
(1, 'A101', 1),
(2, 'A102', 1),
(3, 'B201', 2),
(4, 'L301', 3);
```

#### Insert Data into `Tenants`
```sql
INSERT INTO Tenants (TenantID, TenantName)
VALUES 
(1, 'John Doe'),
(2, 'Jane Smith'),
(3, 'Emily Davis');
```

#### Insert Data into `AptTenants`
```sql
INSERT INTO AptTenants (TenantID, AptID)
VALUES 
(1, 1),
(2, 2),
(3, 4);
```

#### Insert Data into `Requests`
```sql
INSERT INTO Requests (RequestID, Status, AptID, Description)
VALUES 
(1, 'Pending', 1, 'Leaking faucet in kitchen'),
(2, 'Resolved', 2, 'Heating system malfunction'),
(3, 'In Progress', 4, 'Broken window in living room');
```

### Additional Data to Ensure Queries Work

#### Add New Apartments
```sql
INSERT INTO Apartments (AptID, UnitNumber, BuildingID)
VALUES
(5, 'A103', 1),
(6, 'B202', 2);
```

#### Add a New Tenant
```sql
INSERT INTO Tenants (TenantID, TenantName)
VALUES
(4, 'Mark Taylor');
```

#### Associate Tenants with Apartments
```sql
INSERT INTO AptTenants (TenantID, AptID)
VALUES
(1, 2),
(1, 5),
(4, 6);
```

---

## Additional Queries

### View All Tables
```sql
SELECT * FROM Complexes;
SELECT * FROM Buildings;
SELECT * FROM Apartments;
SELECT * FROM Tenants;
SELECT * FROM AptTenants;
SELECT * FROM Requests;
```

---

### Notes
- Use `DROP TABLE table_name;` to delete any table if required.
- Ensure proper foreign key constraints are maintained when inserting or deleting data.
