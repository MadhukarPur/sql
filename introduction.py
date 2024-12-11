'''
What is a database?
    -- A database—Database Management System (DBMS)—is a collection of data organized and stored in a structured format.

    And there are two common types of databases:
        1. Non-Relational
        2. Relational (where SQL is used)

    
    Role of SQL:
        -- SQL is used to interact with and manage data stored in relational databases.
        -- This includes retrieving, inserting, updating, deleting, creating new tables, etc.

    GROUP BY:
        Group By clause is almost always used in conjunction with aggregate functions such as SUM(), MIN(), COUNT() etc. to summarize data.
        
        The GROUP BY clause is used to answer questions such as:
            -- Find the average salary of employees in each department.
            -- Find the number of employees in each department.
            -- Find the maximum and minimum salaries in each department.


    JOINS:

        1. SQL INNER JOIN:
            The SQL INNER JOIN is used to combine rows from two or more tables based on a related column between them.

    
    We can categorize SQL commands into several sublanguages:
        1. Data Query Language (DQL) - SELECT
        2. Data Manipulation Language (DML) - INSERT, UPDATE, DELETE
        3. Data Definition Language (DDL) - CREATE TABLE, CREATE DATABASE, ALTER TABLE, DROP TABLE
        4. Data Control Language (DCL) - GRANT, REVOKE
        5. Transaction Control Language (TCL) - SAVEPOINT, ROLLBACK, COMMIT


    7 must-know strategies to scale your database. 
 
        1 - Indexing: 
            Check the query patterns of your application and create the right indexes. 
        
        2 - Materialized Views: 
            Pre-compute complex query results and store them for faster access. 
        
        3 - Denormalization: 
            Reduce complex joins to improve query performance. 
        
        4 - Vertical Scaling 
            Boost your database server by adding more CPU, RAM, or storage. 
        
        5 - Caching 
            Store frequently accessed data in a faster storage layer to reduce database load. 
        
        6 - Replication 
            Create replicas of your primary database on different servers for scaling the reads. 
        
        7 - Sharding 
            Split your database tables into smaller pieces and spread them across servers. Used for scaling the writes as well as the reads.
'''