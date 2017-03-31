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
			cur.execute("SELECT COUNT(*) FROM ( " + command + " );")
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
	 "SELECT a.name, b.name FROM actor a JOIN movie b JOIN casting where a.a_id < 50;"
	,"SELECT a.name, b.name FROM actor a JOIN movie b JOIN casting where b.m_id < 100;"
	,"SELECT a.name, b.name FROM actor a JOIN movie b JOIN casting where b.year < 2000 and b.year > 1990;"
	,"SELECT a.name, b.name FROM Movie JOIN \"Production Company\" WHERE pc_id < 50;"
	,"SELECT a.name, b.name FROM Movie JOIN \"Production Company\" WHERE \"imdb score\" < 1.5;"
	,"SELECT a.name, b.name FROM Movie JOIN \"Production Company\" WHERE year < 2000 and year > 1950;"
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
