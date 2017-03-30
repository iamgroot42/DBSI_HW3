import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys


def commands(dbname):
	con = psycopg2.connect(dbname=dbname, user='postgres', host='localhost', password='potato')
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor()
	set1 = [
	 "SELECT name FROM movie WHERE imdb score < 2"
	,"SELECT name FROM movie WHERE imdb score between 1.5 and 4.5"
	,"SELECT name FROM movie WHERE year between 1900 and 1990"
	,"SELECT name FROM movie WHERE year between 1990 and 1995"
	]
	for command in set1:
		cur.execute(command)
		cur.execute("SELECT COUNT(*) FROM ( " + command + " );")
	print("Set1 done")
	set2 = [
	 "SELECT name FROM movie WHERE imdb score <= (SELECT MIN (imdb score) FROM movie WHERE year between 1990 and 1995);"
	,"SELECT name FROM movie WHERE imdb score <= ALL (SELECT imdb score FROM movie);"
	]
	for command in set2:
		cur.execute(command)
	print("Set2 done")
	set3 = [
	 "SELECT a.name, b.name FROM actor a JOIN movie b JOIN casting where a.a_id < 50;"
	,"SELECT a.name, b.name FROM actor a JOIN movie b JOIN casting where b.m_id < 100;"
	,"SELECT a.name, b.name FROM actor a JOIN movie b JOIN casting where b.year < 2000 and b.year > 1990;"
	,"SELECT a.name, b.name FROM Movie a JOIN 'Production Company' b WHERE b.pc_id < 50;"
	,"SELECT a.name, b.name FROM Movie a JOIN 'Production Company' b WHERE a.'imdb score' < 1.5;"
	,"SELECT a.name, b.name FROM Movie a JOIN 'Production Company' b WHERE a.year < 2000 and a.year > 1950;"
	]
	for command in set3:
		cur.execute(command)
	print("Set3 done")


if __name__ == "__main__":
	dbname = sys.argv[1]
	commands(dbname)
