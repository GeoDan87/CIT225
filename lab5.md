# Lab 5
1. Consult [Lab 1](https://github.com/GeoDan87/CIT225/blob/main/lab1.md) if necessary. Also make sure that you have Anaconda installed. Once you have Git and Anaconda installed, your going to open Git for Windows. Next we're going to change the directory to Documents by typing  `cd C:\Users\Windows 10\Documents`. Finally you will download the repository using the command `git clone https://github.com/GeoDan87/CIT225.git`. We should be able to clone (and eventually pull from) the repo using HTTPS and avoid the steps of setting up on SSH key.
<br></br>
<br></br>

2. Set up two <u>system</u> environment variables to store you database user name and password; this is what you use to login with HeidiSQL. Environment variables can be set up using the User Interface. You'll store your user name in a variable named MDB_USER and the password in a variable named MDB_PASS. Using environment variables is a best practices way to avoid storing plain text credentials on your system. In real life situations, you might also store the URL or IP Address and other private configuration details as environment variables or using a secrets manager.
<br></br>
<br></br>

3. You're going to open an Anaconda Prompt window, change directories to Documents by typing `cd C:\Users\Windows 10\Documents`. Now we're going to create an anaconda environment that we can use for our labs going forward. To do this, type and run `conda create -n cit225` then `conda activate cit225`. The activate command actually enables us to use this environment. Now we want to install the package manager called pip, so we'll run `conda install pip`. Now that pip is installed, we can run use pip to install the requirements in the requirements.txt file. Make sure that you're still in you Documents folder and then run `pip install -r .\CIT225\requirements.txt`. **Keep your Anaconda window open!**
<br></br>
<br></br>

4. Using the [lab4_create_db.sql](https://github.com/GeoDan87/CIT225/blob/acd5621c5bf35f6fe257212a5d87efca7c1fb7f6/lab4_create_db.sql) file that you now have locally, open the script from HeidiSQL using File > Load SQL File from the menu. Run the file, as I made a few slight changes since the last lab. Finally we're going to run a python script that adds some fake data to your database. In your Anaconda window `python insert_generated_data.py` which was is included in the repository that you cloned.
<br></br>
<br></br>

5. Finally SQL! The first thing we're going to do to is write out by hand a a query that calculates the average age of our supporters. Review at least the date/time functions in the [MariaDB documentation](https://mariadb.com/kb/en/date-time-functions/) to determine which function you would use. Note the number of input arguments and the output. Remember to give your new column an alias.
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

6. Now type this query into a new query tab in HeidiSQL and make any corrections necessary to get it to run. What is the result?
<br></br>
<br></br>

7. Building off of the query from question 5, write out a query by hand that calculates the average age of supporters by country. Then draw out what you would expect your results to look like as a table (using 3 rows and `...` in the 2nd row).
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

8. Run the query from question 7 in new tab in HeidiSQL, but order it with the highest average first. Do the results look like you expected? How many rows were returned? Change your query again and filter the results to only include results over a certain age (you choose).
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

9. That query is great, but we I don't know country codes off the top of my head. Modify the query one last time (removing the HAVING clause you added) so that the results return the name of the country rather than a country code.
<br></br>
<br></br>

Remember our midterm is on Monday!

