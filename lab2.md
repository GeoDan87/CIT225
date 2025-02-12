# Lab 2
## 
1. Review the [Entity Relationship Diagram](https://github.com/GeoDan87/CIT225/blob/e3ea3cb8e5a7db1a4877e7f14cb34fbc1865f57f/lab2_erd.png) (ERD). How does it differ from the ERD that you created last week? Are there different entities, are any of the relationships represented differently, if so, please specify a few?
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

2. Review the attributes of each entity in the ERD, are there attributes in common with those you identified in the last lab? If so, list at least two that you had in common.
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>


3. Review the [documentation of data types](https://mariadb.com/kb/en/data-types/) that is provided by MariaDB. Ideally you should spend 10-15 minutes familiarizing yourself with the datatypes broadly and clicking through on a few.

4. Using your best judgement, for the supporter, the campaign and donation entities determine which data types would be best suited for the attributes (columns) that are shown. Note these data types below.

**supporter**

| Column Name   | Data Type     |
| -------- | ------------- |
| supporter_id | |
| login_id | UUID |
| first_name | |
| last_name | |
| date_of_birth | |
| country | |
| create_timestamp | |
| update_timestamp | |

**campaign**

| Column Name      | Data Type     |
|------------------|---------------|
| campaign_id      |               |
| campaign_type    |               |
| campaign_name    |               |
| campaign_start   |               |
| campaign_end     |               |
| create_timestamp |               |
| update_timestamp |               |

**donation**

| Column Name   | Data Type     |
| -------- | ------------- |
| donation_id | |
| supporter_id | |
| donation_local_currency | varchar(3) |
| donation_local_amount | |
| donation_usd_amount | |
| donation_source | |
| donation_date | |
| donation_status | |
| campaign_id | |
| recurring_donation_id | int |
| create_timestamp | |
| update_timestamp | |

5. We should now start to translate our conceptual model (ERD) to the internal model (DBMS) for the three tables referenced in question 4. We first need to create a database using the following command `CREATE DATABASE hfh;` and then click run or hit F11. Next let build out our Data Definition Language (DDL) statements, terminating each with a semicolon. We'll keep it simple since we know that we're creating the database from scratch and just use CREATE TABLE and the fully qualified name (shown below). If you choose to use any timestamp columns, ensure you've read the documentation about specifically regarding the INSERT and UPDATE behavior. Your can search for "DEFAULT CURRENT_TIMESTAMP" and "ON UPDATE CURRENT_TIMESTAMP".

```
CREATE TABLE hfh.supporter(<column_name> <data_type> [PRIMARY KEY]
                      ,<column_name> <data_type>
                      ,<column_name> <data_type> [FOREIGN KEY 
                      REFERENCES hfh.parent_table(column_name)]);
```
<br></br>
<br></br>
**Please turn in your lab when you are complete. Homework is to read chapter 6.**