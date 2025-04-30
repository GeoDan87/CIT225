# Lab 11
1. The application development is ready to role out a new application that enables supporters to view their donation history to Habitat for Huge Manatees. When using this application, a supporter must be logged into their account and be able to have menus that show human readable information relevant to their donation history. Create a new user for this application using the password `12345678`. Set the password to expire after 6 months. Consult the [MariaDB documentation](https://mariadb.com/kb/en/create-user/) for creating users.
</br>
</br>

2. The password above was chosen because it's easy to remember for the purposes of this lab, but is clearly not a best practice. In the space below, write a <u>security standard</u> for usernames and passwords that are designated for applications.
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

3. Given the description in question 1, write below which tables you think that the application should or needs to have access to?
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
</br>

4. Given the scope of the application described in question 1, what type of privileges should this application be granted to those tables? Consult the [MariaDB documentation](https://mariadb.com/kb/en/grant/#table-privileges) and consider whether the end users of this application require permissions to read and write data
</br>
</br>
</br>

5. Using the `root` user in HeidiSQL, GRANT the privileges that you deemed necessary to the tables that you identified above. Note that you can now use column lists when restricting access to specific columns.
</br>
</br>

6. Keep the original session opened. Open a new HeidiSQL session, in the bottom left of the first menu click '+' and add a new session. Use the credentials that you created in question 1 to login.
</br>
</br>

7. Compare what you can see between the session for the `root` user and the application user, what are a few differences that you can observe? Try running a `SELECT *` query on one of the tables, what happens?
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

8. Using the session logged in as the `root` user, create a view that would show the end user their donation history with human readable descriptions. Add permissions to this view for the application user.
</br>
</br>