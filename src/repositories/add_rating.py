import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

def add_movie_review(user_id, movie_id, rating, comment):
    query = """
        INSERT INTO movie_reviews (user_id, movie_id, rating, comment)
        VALUES (%s, %s, %s, %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, movie_id, rating, comment))

def add_series_review(user_id, series_id, rating, comment):
    query = """
        INSERT INTO series_reviews (user_id, series_id, rating, comment)
        VALUES (%s, %s, %s, %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, series_id, rating, comment))

def add_anime_review(user_id, anime_id, rating, comment):
    query = """
        INSERT INTO anime_reviews (user_id, anime_id, rating, comment)
        VALUES (%s, %s, %s, %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, anime_id, rating, comment))