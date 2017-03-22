# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import numpy as np
# 2014089, 2014021
import random
from random import choice
from string import ascii_lowercase


def random_string(size):
	return ''.join(choice(ascii_lowercase) for i in range(size))


def get_actors(size):
	a_id = range(1,size+1)
	names = []
	for i in range(size):
		names.append(random_string(15))
	return a_id, names


def get_companies(size):
	pc_ids = range(1, size+1)
	names = []
	addresses = []
	for i in range(size):
		names.append(random_string(10))
		addresses.append(random_string(30))
	return pc_ids, names, addresses


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
	return m_ids, names, years, imdb_scores, pc_ids


def get_castings(size, sample):
	m_ids = []
	a_ids = []
	for i in range(1,size+1):
		actors = np.random.choice(sample, 4)
		for actor in actors:
			m_ids.append(i)
			a_ids.append(actor)
	return m_ids, a_ids


if __name__ == "__main__":
	get_actors(200000)
	print "Genarated GenaratedActors database"
	get_companies(50000)
	print "Genarated Companies database"
	get_movies(1000000)
	print "Genarated Movies database"
	get_castings(1000000, 200000)
	print "Genarated Castings database"
