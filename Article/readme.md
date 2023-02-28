# Article

## current data sheet format (`describe`)

### MySQL/MessageBoard:Database/Article_article:Table

```txt
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| Title       | varchar(128) | NO   |     | NULL    |                |
| ReleaseTime | datetime(6)  | NO   |     | NULL    |                |
| Content     | longtext     | NO   |     | NULL    |                |
| Author_id   | int(11)      | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
```

### MySQL/MessageBoard:Database/Article_message:Table

```txt
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| id          | int(11)     | NO   | PRI | NULL    | auto_increment |
| ReleaseTime | datetime(6) | NO   |     | NULL    |                |
| Content     | longtext    | NO   |     | NULL    |                |
| Article_id  | int(11)     | NO   | MUL | NULL    |                |
| Author_id   | int(11)     | NO   | MUL | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
```
