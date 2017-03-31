import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys


def indices(dbname):
	con = psycopg2.connect(dbname=dbname, user='postgres', host='localhost', password='potato')
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor()
	commands = [
	 "CREATE INDEX ON Actor USING btree(name)"
	,"CREATE INDEX ON Movie USING btree(name)"
	,"CREATE INDEX ON Movie USING btree(year)"
	,"CREATE INDEX ON Movie USING btree(\"imdb score\")"
	,"CREATE INDEX ON Movie USING btree(\"production company\")"
	,"CREATE INDEX m_id ON Casting USING btree"
	,"CREATE INDEX a_id ON Casting USING btree"
	]
	for command in commands:
		cur.execute(command + ";")
		print("Made an index")

if __name__ == "__main__":
	dbname = sys.argv[1]
	indices(dbname)
