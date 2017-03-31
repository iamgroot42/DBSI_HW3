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
* `python push_data.py <dbname>` to populate tables wih synthetic data from defined distributions.
* `python make_indices.py <dbname>` to make btree indices for these tables.
* `python run_queries.py <dbname` to run queries and see their outputs.


### Description


Actor:
	a_id [1,200000]
	name [15string]	

Production Company:
	pc_id [1,50000]
	name [10string]
	address [30string]

Movie:
	m_id [1,1000000]
	name [10string]
	year [1900,2000]
	imdb score [1.0,5.0] (95% of scores in [1.0,2.0], 5% of scores in (2.0,5.0]
	pc_id ( 90% are in [1,100], 10% are in [11,50000])

Casting:
	m_id
	a_id

Each movie has 4 actors, all movies have actors

Indices (btree) on:
	actor table name
	name in movie table
	year in movie
	m_id in Casting
	a_id in casting
