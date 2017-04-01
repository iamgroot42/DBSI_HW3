import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys


def create_db(dbname):
	con = psycopg2.connect(dbname='postgres', user='postgres', host='localhost', password='potato')
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor()
	created = True
	try:
		cur.execute('CREATE DATABASE ' + dbname)
	except:
		created = False
	cur.close()
	return created


def create_tables(dbname):
	con = psycopg2.connect(dbname=dbname, user='postgres', host='localhost', password='potato')
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor()
	table_commands = [
		"""
		CREATE TABLE Actor (
		a_id INTEGER PRIMARY KEY,
		name VARCHAR(15) NOT NULL,
		CHECK (a_id >= 1 AND a_id <= 200000)
		)
		""",
		"""
		CREATE TABLE ProductionCompany (
			pc_id INTEGER PRIMARY KEY,
			name VARCHAR(10) NOT NULL,
			address VARCHAR(30) NOT NULL,
			CHECK (pc_id >= 1 AND pc_id <= 50000)
		)
		""",
		"""
		CREATE TABLE Movie (
			movie_id INTEGER PRIMARY KEY,
			name VARCHAR(10) NOT NULL,
			year SMALLINT,
			"imdb score" DECIMAL,
			"production company" INTEGER REFERENCES ProductionCompany(pc_id),
			CHECK (movie_id >= 1 AND movie_id <= 1000000),
			CHECK (year >= 1900 AND year <= 2000),
			CHECK ("imdb score" >= 1.0 AND "imdb score" <= 5.0)
		)
		""",
		"""
		CREATE TABLE Casting (
			a_id INTEGER REFERENCES Actor(a_id),
			m_id INTEGER REFERENCES Movie(movie_id),
			PRIMARY KEY (a_id, m_id)
		)
		"""
	]
	created = True
	for command in table_commands:
		try:
			cur.execute(command)
		except:
			created = False
	cur.close()
	return created


def clean_slate(dbname):
	con = psycopg2.connect(dbname=dbname, user='postgres', host='localhost', password='potato')
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor()
	tablenames = ["Casting", "Movie", "Production Company", "Actor"]
	dropped = True
	for tablename in tablenames:
		try:
			cur.execute("DROP TABLE " + tablename + " ;")
		except:
			dropped = False
	cur.close()
	return dropped


if __name__ == "__main__":
	dbname = sys.argv[1]
	if create_db(dbname):
		print("Database created")
	if clean_slate(dbname):
		print("Tables cleared")
	if create_tables(dbname):
		print("Tables created")
