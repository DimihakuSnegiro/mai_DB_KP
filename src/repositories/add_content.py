import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

def add_movie(title, description, release_year, duration, director, country, language, genre):
    query = """
        INSERT INTO movies (title, description, release_year, duration, director, country, language, genre)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (title, description, release_year, duration, director, country, language, genre))

def add_series(title, description, release_year, number_of_seasons, number_of_episodes, creator, country, language, genre):
    query = """
        INSERT INTO series (title, description, release_year, number_of_seasons, number_of_episodes, creator, country, language, genre)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (title, description, release_year, number_of_seasons, number_of_episodes, creator, country, language, genre))

def add_anime(title, description, release_year, number_of_episodes, studio, genre, country, language):
    query = """
        INSERT INTO anime (title, description, release_year, number_of_episodes, studio, genre, country, language)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (title, description, release_year, number_of_episodes, studio, genre, country, language))