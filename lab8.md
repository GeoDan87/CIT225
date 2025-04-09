# Lab 8
1. In our last lecture we learned about the SQL optimizer, how our DBMS make decisions about executing our queries and how can we can tune the performance of our queries. First, write and run queries that select all of the statistics from the tables in the hfh database. The statistics are stored in the `information_schema.statistics` table and the `information_schema.innodb_sys_tablestats` table. What type of data/information is included in these table? Are there any columns you have questions about?
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

2. The Habitat for Huge Manatees Fundraising Team wants to know: which supporters (by supporter_id for now) were, but no longer are sustaining donors, how long (in years) they were sustaining donors for and what was the total dollar (USD) amount that they gave over the duration of their sustaining membership? In the space below draw out the structure of the table that would need to be returned to satisfy this request.
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

3. For question 2, which tables from the hfh database would be needed?
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

4. In HeidiSQL, start by closing all existing query tabs. Write out the query that will produce the results you drew out in question 1. Click run or push `F9` and debug the query until you can get it to complete. 
<br></br>

5. Add the `EXPLAIN` statement to the top of your query. In a new query tab, copy the same query and change the `EXPLAIN` statement to an `ANALYZE` statement. What difference do you notice in terms of the output of the tabular output of adding these statements? You can consult the [MariaDB EXPLAIN documentation](https://mariadb.com/kb/en/explain/) and [MariaDB ANALYZE documentation](https://mariadb.com/kb/en/analyze-statement/).
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

6. Alter the `ANALYZE` statement to `ANALYZE FORMAT=JSON` and run it again. Note a greater level of detail included in the JSON results. You can double click on the json results to see them in a larger pop out.
<br></br>

7. Close the query tab with the `ANALYZE` statement (keeping open the one with the `EXPLAIN` statement). Delete the `EXPLAIN` statement and replace it with `SET optimizer_trace = 'enabled = on';`. Then after your query add `SELECT * FROM information_schema.optimizer_trace`. In these steps we're enabling a trace of the optimizer, so that we can gain a better understanding of what decisions are being made and how our query is being executed. You're welcome to review this [nifty resource](https://mariadb.org/wp-content/uploads/2020/09/optimizer-trace_serverfest2020.pdf) to learn more about our optimizer trace and also how/where the analyze and explain fit in. 
