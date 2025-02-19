# Lab 3
1. Go to the github repo for our class and download the [create_db.sql](https://github.com/GeoDan87/CIT225/blob/4901941a606905f5e6e3462ddc7c894d11427c37/create_db.sql) file.
    - You could also clone the repo to your virtual machine if you know how.
    - Open HeidiSQL and run the code by click the "Play button" or hitting F9.

2. Create a dependency diagram for the newsletter_subscription table. 
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
    - Which type of dependencies/dependency were they?
<br></br>
<br></br>
<br></br>
<br></br>
    - Between which columns did the dependency/dependencies exist?
<br></br>
<br></br>
<br></br>
<br></br>
    - What might be a remedy?
<br></br>
<br></br>
<br></br>
<br></br>

3. We're still missing several tables from our database, by looking at columns in the existing tables, can you identify which tables might need to be added?
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

4. Make a copy of the SQL script in a new query window. Change around the order of the create table statements, did any issues arise? Why might this be?
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

5. Let's create the missing tables:

**donation_status**

| Column Name          | Data Type     | Primary Key   |
|----------------------|---------------|---------------|
| donation_status      |  int          | X             |
| donation_status_desc |  varchar(100) |               |
| create_timestamp     |  timestamp    |               |
| update_timestamp     |  timestamp    |               |

**sustaining_status**

| Column Name            | Data Type     | Primary Key   |
|------------------------|---------------|---------------|
| sustaining_status      |  int          | X             |
| sustaining_status_desc |  varchar(100) |               |
| create_timestamp       |  timestamp    |               |
| update_timestamp       |  timestamp    |               |

**country**

| Column Name      | Data Type     | Primary Key   |
|------------------|---------------|---------------|
| country_code     |  varchar(3)   | X             |
| country_name     |  varchar(100) |               |
| create_timestamp |  timestamp    |               |
| update_timestamp |  timestamp    |               |

**language**

| Column Name      | Data Type     | Primary Key   |
|------------------|---------------|---------------|
| language_code    |  varchar(3)   | X             |
| language_name    |  varchar(100) |               |
| create_timestamp |  timestamp    |               |
| update_timestamp |  timestamp    |               |

**local_currency**

| Column Name            | Data Type     | Primary Key   |
|------------------------|---------------|---------------|
| local_currency         |  varchar(3)   | X             |
| local_currency_name    |  varchar(100) |               |
| create_timestamp       |  timestamp    |               |
| update_timestamp       |  timestamp    |               |

**campaign_type**

| Column Name          | Data Type     | Primary Key   |
|----------------------|---------------|---------------|
| campaign_type        |  int          | X             |
| campaign_type_desc   |  varchar(100) |               |
| create_timestamp     |  timestamp    |               |
| update_timestamp     |  timestamp    |               |

6. Alter the tables and foreign key constraints to the proper tables.
```
ALTER TABLE IF EXISTS database.table
    ADD CONSTRAINT `constraint_name` FOREIGN KEY (column_name) REFERENCES database.table(column_name)
                    ON DELETE CASCADE
                    ON UPDATE RESTRICT
```
