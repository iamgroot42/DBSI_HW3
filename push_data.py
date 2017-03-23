import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import numpy as np
import sys
import random
from random import choice
from string import ascii_lowercase
from progressbar import ProgressBar
# 2014089, 2014021


def random_string(size):
	return ''.join(choice(ascii_lowercase) for i in range(size))


def get_actors(size):
	a_id = range(1,size+1)
	names = []
	for i in range(size):
		names.append(random_string(15))
	print("Data for Actor generated")
	return (a_id, names)


def get_companies(size):
	pc_ids = range(1, size+1)
	names = []
	addresses = []
	for i in range(size):
		names.append(random_string(10))
		addresses.append(random_string(30))
	print("Data for Production Company generated")
	return (pc_ids, names, addresses)


def get_movies(size):
	m_ids = range(1, size+1)
	names = []
	years = []
	imdb_scores = []
	pc_ids = []
	for i in range(size):
		names.append(random_string(10))
		years.append(random.randint(1900,2000))
	for i in range(int(0.95*size)):
		imdb_scores.append(np.random.rand() + 1.0)
	for i in range(int(size - (0.95*size))):
		imdb_scores.append(np.random.rand()*3.0 + 2.0)
	random.shuffle(imdb_scores) 
	for i in range(int(0.90*size)):
		pc_ids.append(np.random.randint(1,10))
	for i in range(int(size - (0.90*size))):
		pc_ids.append(np.random.randint(11,50000))
	random.shuffle(pc_ids)
	print("Data for Movie generated")
	return (m_ids, names, years, imdb_scores, pc_ids)


def get_castings(size, sample):
	m_ids = []
	a_ids = []
	for i in range(1,size+1):
		actors = np.random.choice(sample, 4)
		for actor in actors:
			m_ids.append(i)
			a_ids.append(actor)
	print("Data for Casting generated")
	return (m_ids, a_ids)


def push_to_table(dbname, data, ttype):
	con = psycopg2.connect(dbname=dbname, user='postgres', host='localhost', password='potato')
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor()
	pbar = ProgressBar()
	done = False
	print("Populating "+ ttype)
	if ttype == "Actor":
		a_ids, names = data
		query =  "INSERT INTO Actor (a_id, name) VALUES (%s, %s);"
		for i in pbar(range(len(a_ids))):
			data = (a_ids[i], names[i])
			cur.execute(query, data)
		done = True
	elif ttype == "Production Company":
		pc_ids, names, addresses = data
		query =  "INSERT INTO \"Production Company\" (pc_id, name, address) VALUES (%s, %s, %s);"
		for i in pbar(range(len(pc_ids))):
			data = (pc_ids[i], names[i], addresses[i])
			cur.execute(query, data)
		done = True
	elif ttype == "Movie":
		m_ids, names, years, imdb_scores, pc_ids = data
		query =  "INSERT INTO Movie (movie_id, name, year, \"imdb score\", \"production company\") VALUES (%s, %s, %s, %s, %s);"
		for i in pbar(range(len(m_ids))):
			data = (m_ids[i], names[i], years[i], imdb_scores[i], pc_ids[i])
			cur.execute(query, data)
		done = True
	else:
		a_ids, m_ids = data
		query =  "INSERT INTO Casting (a_id, m_id) VALUES (%s, %s);"
		for i in pbar(range(len(a_ids))):
			data = (a_ids[i], m_ids[i])
			cur.execute(query, data)
		done = True
	if done:
		print("Succesfully populated " + ttype + " database")
	return done


if __name__ == "__main__":
	dbname = sys.argv[1]
	push_to_table(dbname, get_actors(200000), 'Actor')
	push_to_table(dbname, get_companies(50000), 'Production Company')
	push_to_table(dbname, get_movies(1000000), 'Movie')
	push_to_table(dbname, get_castings(1000000, 200000), 'Casting')
