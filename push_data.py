import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

import numpy as np

# 2014089, 2014021

# Actor:
# 	a_id [1,200000]
# 	name [15string]	

# Production Company:
# 	pc_id [1,50000]
# 	name [10string]
# 	address [30string]

# Movie:
# 	m_id [1,1000000]
# 	name [10string]
# 	year [1900,2000]
# 	imdb score [1.0,5.0] (95% of scores in [1.0,2.0], 5% of scores in (2.0,5.0]
# 	pc_id ( 90% are in [1,100], 10% are in [11,50000])

# Casting:
# 	m_id
# 	a_id

# Each movie has 4 actors, all movies have actors

# Indices on:
# 	actor table name
# 	name in movie table
# 	year in movie
# 	m_id in Casting
# 	a_id in casting