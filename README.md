# DBSI_HW3


### Setting it up
Run the folliwng commands (in order):

* `sudo apt-get install postgresql postgresql-contrib` to install postgresql on ubuntu16
* `sudo pip install psycopg2` to install thr python-wrapper for postgresql
* `sudo -i -u postgres` to switch to postgres user (for manaing postgresql)
* `psql` to run postgresql CLI
* `ALTER USER "postgres" WITH PASSWORD 'potato';` to change the default password 



### Running it

* `python populate_tables.py <dbname>` to create a database 'dbname' and create tables appropriately.
