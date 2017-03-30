import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys


def indices(dbname):
	con = psycopg2.connect(dbname=dbname, user='postgres', host='localhost', password='potato')
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor()
	tablenames = ["Casting", "Movie", "\"Production Company\"", "Actor"]
	for tablename in tablenames:
		command = "CREATE INDEX  ON " + tablename + " USING btree"


if __name__ == "__main__":
	dbname = sys.argv[1]
	indices(dbname)
