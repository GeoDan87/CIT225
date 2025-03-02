---
marp: true
---

# Lesson 8: More SQL
---
# Getting Unique Values
- There are many use cases for being able to query the unique values from a specific column.
- We use the DISTINCT clause give us a results set of only the unique value of a specific column
```
/*Return the unqiue values from the id_column column*/
SELECT DISTINCT id_column
FROM database.table
```
---
# Aggregate Functions
- These functions are used in with the `SELECT` command to provide a mathematical summary of the data
- A column name is the only argument that is passed to these functions
- Make sure that you read the documentation to understand how NULL values are treated by these functions
---
# Aggregate Functions continued
| Function | Definition                                            | General Data Types |
|----------|-------------------------------------------------------|--------------------|
| COUNT()  | The number of rows in a results set                   | Any                |
| MIN()    | The minimum value in a given column                   | Numeric            |
| MAX()    | The maximum value in a given column                   | Numeric            |
| SUM()    | The sum of all values in a given column               | Numeric            |
| AVG()    | The average or mean of all values in a given column   | Numeric            |            
---
# ORDER BY Clause
- We've discussed the `SELECT` command and the need to have a `FROM` clause and the option to have a `WHERE` clause
- There are some more optional clauses that you can have when you're querying data
- One of these is the `ORDER BY`, which as it sounds orders your results set
---
# ORDER BY Clause continued
- Order by can sort data in `ASCENDING` (small to large) or `DESCENDING` (large to small)
    - The default order depends on the DBMS, but is generally ascending
    - These keywords can also be shortended to `ASC` and  `DESC`
- Keep in mind that the placement of NULL values is determined by the DBMS
---
# GROUP BY Clause
- There are lots of times where we want to summarize our data by different groups, rather than generally (aggregate function only)
- For these cases, we use the `GROUP BY` clause to define the column(s) that we want to group our data by
- The other columns that are defined in the `SELECT` that are not in the `GROUP BY` must be defined with an aggregate function.
```
SELECT id_column
       ,SUM(value_column)
FROM database.table
GROUP BY id_column
```
---
# HAVING Clause
- This is an optional clause that is used in conjunction with a `GROUP BY` clause
    - It cannot be used without a `GROUP BY` clause!
- Think of it as a way of filtering your grouped results or a `WHERE` clause for your `GROUP BY`
```
SELECT id_column
       ,SUM(value_column)
FROM database.table
GROUP BY id_column
HAVING SUM(valuue_column) > 10
```
---
# Query Definition vs. Execution Order
| Command/Clause | Query Order | Execution Order |
|----------------|-------------|-----------------|
| SELECT         | 1           | 5               |
| FROM           | 2           | 1               |
| WHERE          | 3           | 2               |
| GROUP BY       | 4           | 3               |
| HAVING         | 5           | 4               |
| ORDER BY       | 6           | 6               |
---
# Joining Tables
- In data modeling and the creation of our ERD and subsquently our database, we've done a lot of work ensuring referential integrity between our entities
- Normalized data doesn't  always make sense to end users, so we need to denormalize that data
    - We typically do this by joining different entities together
- **Please ignore section 7-7 (pg 300-304) in the book, we shouldn't join tables this way!**
- **Please also ignore section 8-1c (pg 344), we won't do joins with USING!**
---
# Joining Tables Continued
| Join Type      | Description                  |
|----------------|------------------------------|
| OUTER JOIN     | A join in which all matching records between two or more tables are retained |
| INNER JOIN     | |
| NATURAL JOIN   | |
| CROSS JOIN     | |