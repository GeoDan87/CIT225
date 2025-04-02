1. Last lab we worked through trying to implement a trigger in the database to track changes in the donation status. Let's pull the updates from the CIT225 repo, so open Git Bash and cd to the directory where CIT225 is. Run the following command `git pull origin main`, this will copy the contents of the remote repository to your virtual machine.

2. Now that we have the updated code base, we'll open Anaconda prompt and type `conda activate CIT225` then run `pip install dateutils`. In the directory containing your CIT225 folder you'll run `python insert_generated_data_lab7.py`.
<br></br>
<br></br>

3. Write and run queries to drop the audit table and trigger that you created last week during lab. Now open and run the lab7.sql file. What is different between the trigger that is now implemented and the one that you wrote last week?
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

4. Now we want check the current transaction isolation set for the database. In this case, the value is stored in a global variable (assigned with `@@`). We'll use a `SELECT` statement without a `FROM` by writing and executing the command `SELECT @@transaction_isolation`. What is the transaction isolation level that is set by the database?
<br></br>
<br></br>
<br></br>

5. Let's learn about how locking works and how the isolation levels play into this. First, select the a row of the `hfh.donation` table with a `donation_id = 1`. <u> Keep this query open!</u> What is the `donation_status` for this record?
<br></br>
<br></br>
<br></br>

6. Open a second HeidiSQL session, so that you have two sessions open. Copy and run the following transaction in the original session. In the second session, copy and run exactly the same transaction. What happened?
```
START TRANSACTION;
/*Turn off autocommit so an explicit commit is needed*/
SET autocommit = 0;

UPDATE hfh.donation
/*Check that the current status is not 4, if it is, change it to something else*/
SET donation_status = 4
WHERE donation_id = 1;
```
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

7. Run the select query from question 5 that you kept open in the first session, what is the value of the `donation_status` column?
<br></br>
<br></br>
<br></br>

8. In the second session run the same query from question 5, what is the value of the `donation_status` column? Why do you think this happened?
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

9. You can manipulate the isolation that you queried in question 4. In your second session, add the following line at the top of the query from question 5. `SET SESSION transaction_isolation = 'read-uncommitted';`, run the query. What is the result now?
<br></br>
<br></br>
<br></br>
