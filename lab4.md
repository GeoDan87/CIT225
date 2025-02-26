# Lab 4
1. Download or copy and run then run the lab4_create_db.sql file from github.
<br></br>

2. We're going to use the SELECT command to query data from a (fully qualified) table called information_schema.columns. Hand write a SQL query that returns all rows from this table.
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

3. Type the command you wrote out into your HeidiSQL client. Let's add the following WHERE clause `WHERE table_schema = 'hfh'`. Describe the data that is returned, how many rows, what type of data does this appear to be?
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

4. Write out an INSERT command by hand that adds data into the hfh.podcast table. We want to add the following rows of data.

| podcast_name               | start_date | end_date   |
| -------------------------- | ---------- | ---------- |
| The Joe Dugong Experience  | 2024-01-01 | NULL       |
| Toothless                  | 2021-02-10 | NULL       |
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>


5. Write out an UPDATE command to add descriptions and languages for the rows that were previously added to the hfh.podcast table.

| podcast_name               | podcast_description                                                | lang_code |
| -------------------------- | ------------------------------------------------------------------ | --------- |
| The Joe Dugong Experience  | Joe Smith discusses dugongs and their habitats.                    |   eng     |
| Toothless                  | Will, Jason and Sean discuss the lack of canine and incisor teeth. |   eng     |
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

6. In separate windows, write the INSERT command in HeidiSQL and run it. Do the same for the UPDATE command and then run it. Were there issues running either of these SQL DML statements? If so, what do you suspect caused the problem?
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

When you're done, turn your lab in. Remember to read chapters 7 and 8!

