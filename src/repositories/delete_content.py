import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

def delete_movie(title):
    query = """
        DELETE FROM movies WHERE title = %s;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (title,))

def delete_series(title):
    query = """
        DELETE FROM series WHERE title = %s;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (title,))

def delete_anime(title):
    query = """
        DELETE FROM anime WHERE title = %s;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (title,))

def delete_movie_rating(movie_id):
    query = """
        DELETE FROM movie_ratings
        WHERE movie_id = %s;

        DELETE FROM movie_reviews
        WHERE movie_id = %s;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (movie_id, movie_id))

def delete_series_rating(series_id):
    query = """
        DELETE FROM series_ratings
        WHERE series_id = %s;

        DELETE FROM series_reviews
        WHERE series_id = %s;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (series_id, series_id))

def delete_anime_rating(anime_id):
    query = """
        DELETE FROM anime_ratings
        WHERE anime_id = %s;

        DELETE FROM anime_reviews
        WHERE anime_id = %s;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (anime_id, anime_id))
