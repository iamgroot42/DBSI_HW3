import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys


def commands(dbname):
	con = psycopg2.connect(dbname=dbname, user='postgres', host='localhost', password='potato')
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor()
	set1 = [
	 "SELECT name FROM movie WHERE \"imdb score\" < 2"
	,"SELECT name FROM movie WHERE \"imdb score\" between 1.5 and 4.5"
	,"SELECT name FROM movie WHERE year between 1900 and 1990"
	,"SELECT name FROM movie WHERE year between 1990 and 1995"
	]
	try:
		for command in set1:
			cur.execute("EXPLAIN ANALYZE " + command + ";")
			print(cur.fetchall())
			raw_input("Done")
			cur.execute("SELECT COUNT(*) FROM (" + command + ") AS foo;")
			print(cur.fetchall())
			raw_input("Done")
		print("Set1 done")
	except:
		print("Set1 queries incomplete")
	set2 = [
	 "SELECT name FROM movie WHERE \"imdb score\" <= (SELECT MIN (\"imdb score\") FROM movie WHERE year between 1990 and 1995);"
	,"SELECT name FROM movie WHERE \"imdb score\" <= ALL (SELECT \"imdb score\" FROM movie);"
	]
	try:
		for command in set2:
			cur.execute("EXPLAIN ANALYZE " + command + ";")
			print(cur.fetchall())
			raw_input("Done")
		print("Set2 done")
	except:
		print("Set2 queries incomplete")
	set3 = [
	 "SELECT Actor.name, Movie.name FROM Actor JOIN Movie JOIN Casting where Actor.a_id < 50"
	,"SELECT Actor.name, Movie.name FROM Actor JOIN Movie JOIN Casting where Movie.m_id < 100"
	,"SELECT Actor.name, Movie.name FROM Actor JOIN Movie JOIN Casting where Movie.year between 1990 and 2000"
	,"SELECT Actor.name, \"Production Company.name\" FROM Movie JOIN \"Production Company\" WHERE \"Production Company.pc_id\" < 50"
	,"SELECT Actor.name, \"Production Company.name\" FROM Movie JOIN \"Production Company\" WHERE \"Actor.imdb score\" < 1.5"
	,"SELECT Actor.name, \"Production Company.name\" FROM Movie JOIN \"Production Company\" WHERE Actor.year BETWEEN 1950 and 2000"
	]
	try:
		for command in set3:
			cur.execute("EXPLAIN ANALYZE " + command + ";")
			print(cur.fetchall())
			raw_input("Done")
		print("Set3 done")
	except:
		print("Set3 queries incomplete")


if __name__ == "__main__":
	dbname = sys.argv[1]
	commands(dbname)
