# Simple Data Migration
## Guide to use this  app
This is a simple migration application from Oracle to Mariadb. 
The migration process only limited to:
- Basic datatype (Varchar and Number)
- Only one schema can be converted.

## Requirements for the app

- Pip for installing [cx_Oracle](https://oracle.github.io/python-cx_Oracle/) and [mariadb](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/)
- [Oracle instant client](https://www.oracle.com/database/technologies/instant-client/downloads.html)
- MariaDB and Oracle database

## Step 0: Export Environment Variables
Authentication details needed for Mariadb and Oracle connections.  
 
#### Example Export ENV Variables
#### Oracle
```
    HOSTNAME= localhost
    ORACLE_SID= orclcdb [ name of a specific database instance ]
    ORACLE_PID= orclpdb1 [ name of a pluggable database created using sysdba ]  
    ORACLE_USER= user 
    ORACLE_U=PWD= password
```
#### Mariadb
```
    HOSTNAME= localhost
    MARIADB_USER= user
    MARIADB_PWD= password
    MARIADB_DB= dbname [Your database name created in MariaDB]
```



## Step 1: migrate schema
Assuming data and tables already created and inserted within  the limitations. Run the mirgateschema.py

## Step 2: migrate data
To run python  mirgatedata.py, staging path is a windows directory path for storing temporary csv files to be loaded into MariaDB
. If is not a windows directory path, a variable named `path = path.replace("\\",'/')` need to be removed.
```
staging_path = rf'C:user\staging_data\table\{datetime.now().date().__str__()}
````
## In progress work
BLOB and CLOB migrations
