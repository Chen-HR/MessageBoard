# Account

## current data sheet format (`describe`)

### MySQL/MessageBoard:Database/Account_user:Table

```txt
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| Account  | varchar(32)  | NO   |     | NULL    |                |
| Password | varchar(32)  | NO   |     | NULL    |                |
| Name     | varchar(64)  | NO   |     | NULL    |                |
| Phone    | varchar(64)  | NO   |     | NULL    |                |
| Email    | varchar(256) | NO   |     | NULL    |                |
| Jointime | datetime(6)  | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```

## future

Afterwards try converting to use "[Django auth](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/)", Can improve the function of user management.

### MySQL/MessageBoard:Database/auth_user:Table

```txt
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int(11)      | NO   | PRI | NULL    | auto_increment |
| password     | varchar(128) | NO   |     | NULL    |                |
| last_login   | datetime(6)  | YES  |     | NULL    |                |
| is_superuser | tinyint(1)   | NO   |     | NULL    |                |
| username     | varchar(150) | NO   | UNI | NULL    |                |
| first_name   | varchar(30)  | NO   |     | NULL    |                |
| last_name    | varchar(150) | NO   |     | NULL    |                |
| email        | varchar(254) | NO   |     | NULL    |                |
| is_staff     | tinyint(1)   | NO   |     | NULL    |                |
| is_active    | tinyint(1)   | NO   |     | NULL    |                |
| date_joined  | datetime(6)  | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
```
