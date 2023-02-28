# main for Python3-Django-MessageBoard

## Basic

```bash
sudo apt update -y ; sudo apt upgrade -y ;
```

## Install

```bash
sudo apt install mariadb-server -y ;
sudo apt install python3-django -y ;
sudo apt install libmariadb-dev -y ;
sudo apt install python3-dev -y ;
sudo apt install python3-mysqldb -y ;
```

```bash
sudo apt install mariadb-server -y ; sudo apt install python3-django -y ; sudo apt install libmariadb-dev -y ; sudo apt install python3-dev -y ; sudo apt install python3-mysqldb -y ;
```

## setup mariadb (MySQL)

```bash
sudo mysql_secure_installation
```

```txt
$ sudo mysql_secure_installation

NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

In order to log into MariaDB to secure it, we'll need the current
password for the root user.  If you've just installed MariaDB, and
you haven't set the root password yet, the password will be blank,
so you should just press enter here.

Enter current password for root (enter for none): 
OK, successfully used password, moving on...

Setting the root password ensures that nobody can log into the MariaDB
root user without the proper authorisation.

You already have a root password set, so you can safely answer 'n'.

Change the root password? [Y/n] n
 ... skipping.

By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

Remove anonymous users? [Y/n] n
 ... skipping.

Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n] Y
 ... Success!

By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.

Remove test database and access to it? [Y/n] n
 ... skipping.

Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

Reload privilege tables now? [Y/n] Y
 ... Success!

Cleaning up...

All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!
```

## setup project

```bash
#!/bin/bash
django-admin startproject MessageBoard
mkdir MessageBoard/templates
mkdir MessageBoard/static

cd MessageBoard
python3 manage.py startapp Account
python3 manage.py startapp Article
```

### in `MessageBoard/MessageBoard/settings.py`

```python
LANGUAGE_CODE = 'zh-hant'
```

```python
TIME_ZONE = 'Asia/Taipei'
```

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Account',
    'Article',
]
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MessageBoard',
        'USER': 'MessageBoard_admin',
        'PASSWORD': 'MessageBoard_admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Set MySQL

```bash
sudo mysql -u root -p
```

```sql
create database MessageBoard;

create user 'MessageBoard_Admin_Account'@'localhost' identified by 'MessageBoard_Admin_Password';
grant ALL PRIVILEGES on MessageBoard.* to 'MessageBoard_Admin_Account'@'localhost';
flush PRIVILEGES;
exit;
```

```bash
sudo mysql -u MessageBoard_Admin_Account -p
```
