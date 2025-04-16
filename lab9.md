# Lab 9
1. First, use a DDL statement to create a copy of the `hfh.supporter` table called `hfh.supporter_copy`, be sure to change the name of the foreign key.
</br>
</br>

2. Conveniently enough, MariaDB has syntax that allows us to more easily copy the schema from an existing table to a new table. Open a new query tab and first `DROP TABLE hfh.supporter_copy;` Then create the table again, but use the following syntax: `CREATE TABLE hfh.supporter_copy LIKE hfh.supporter`.
</br>
</br>

3. Now, write a transaction that selects all of the rows from the `hfh.supporter` table and inserts them into the `hfh.supporter_copy` table. You may need to change the delimiter from a semi-colon to something such as `$$`. Debug the transaction until you get it to run.
</br>
</br>

4. Write one or more queries to verify that the count of rows in the `hfh.supporter` and `hfh.supporter_copy` tables are equal.
</br>
</br>

5. Temporary tables can have many uses, such as copying around data to populate new or existing tables. They are created the same way as a regular table but use the keyword "TEMPORARY" like `CREATE TEMPORARY TABLE`. Now let's create a temporary table called `hfh.supporter_temp` that shares the schema of `hfh.supporter` table. 
</br>
</br>

6. Keeping the original session opened, open a new session of HeidiSQL. Run the following command in both sessions `SHOW TABLES FROM hfh;`. Do you notice any differences between the tables in each of sessions?
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>

7. Read the [MariaDB](https://mariadb.com/kb/en/create-table/) documentation about temporary tables. What is the reason for the difference that you observed in question 6?
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>