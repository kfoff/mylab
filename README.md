## Quick use
```bash
python3 mylab help
mkdir bar && cd bar
python3 mylab init foo bar
python3 mylab all
python3 mylab start
```


## Step by step use (Linux)

Create new directory and go to it.
```bash
mkdir bar && cd bar
```



Init ```config.json``` with arguments.


```bash
python3 mylab init foo bar
```
> "foo" it is owner **https://github.com/foo**,
> "bar" it is repository **https://github.com/foo/bar**,


Clone project from github **https://github.com/foo/bar**:
```bash
python3 mylab clone
```



Create environment and install pip modules.
```bash
python3 mylab install
```



Create databases and migrate data.
```bash
python3 mylab makemigrate
```



Load data from ```xml``` to database.
```bash
python3 mylab load
```


Copy media.
```bash
python3 mylab media
```


Change password for superuser.
```bash
python3 mylab perm
```


Start project.
```bash
python3 mylab start
```
or
```bash
python3 mylab start 8002
```
or
```bash
python3 mylab manage runserver_plus 0.0.0.0:8002 --settings dj.settings_nsk
```
> port from ```8000``` to ```8500```

Running on: **http://mylab.babah24.ru:8002**

## Installation (Windows)

The initial structure of your project should look like this:

- working_dir/
    - assets/
        - media/ - the project's media
        - dump/ - the project's dump
    - mylab

Requirements you will need to run Mylab under Windows:

1) Install Python3:
https://www.python.org/ftp/python/3.6.8/python-3.6.8-..

Type "python" into the CMD to make sure that it's accessible from the command line, if it doesn't work,
add your python path to the PATH env variable

2) Install Git:
https://github.com/git-for-windows/git/releases/downl..

Also make sure that's accessible from the CMD by typing "git"
if it is not, **add "C:\Program Files\Git\cmd;",** to the end of your PATH variable

3) Install PostgreSQL (11 Version)
https://www.enterprisedb.com/downloads/postgres-postg..

Make sure, that "psql" is accessible from the CMD
if it is not, **add "C:\Program Files\PostgreSQL\11\bin;" ** to the end of your PATH variable

edit your **C:/Program Files/PostgreSQL/11/data/pg_hba.conf file**, replace the values in the last column with the values 'trust' like this:


```
host all all 127.0.0.1/32 trust
host all all ::1/128 trust
host replication all 127.0.0.1/32 trust
host replication all ::1/128 trust
```

4) Install MSYS2 
http://www.msys2.org/

5) Install GTK+ 3

Open a MSYS2 MinGW shell, and run: pacman -S mingw-w64-x86_64-gtk3

6) Modify PATH variable so that the library can be found

Open up Control Panel
Go to System and Security > System
Click on the Advanced system settings link
Click on Environment Variables... button
Under System variables find the Path variable and select it
Click the Edit button
Add C:\msys32\mingw64\bin; to the end of the PATH variable, depending on your system architecture
Click OK, and you are done

7) Restart your system for the changes to apply

## Step be step use (Windows)

Clone Mylab and go to its directory
```bash
git clone git@github.com:kfoff/mylab.git && cd mylab
```
Init ```config.json``` with arguments.
```bash
python mylab init foo bar
```
> "foo" it is owner **https://github.com/foo**,
> "bar" it is repository **https://github.com/foo/bar**,

Start the full installation of the chosen repository
```bash
python mylab all
```

After the installation, start the server
```bash
python mylab start <port (optional)>
```
