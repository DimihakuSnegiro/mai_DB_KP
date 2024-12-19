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

def delete_movie_review(user_id, movie_id):
    query = """
            DELETE FROM movie_reviews 
            WHERE user_id = %s AND movie_id = %s;
        """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, movie_id))


def delete_series_review(user_id, series_id):
    query = """
            DELETE FROM series_reviews 
            WHERE user_id = %s AND series_id = %s;
        """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, series_id))


def delete_anime_review(user_id, anime_id):
    query = """
            DELETE FROM anime_reviews 
            WHERE user_id = %s AND anime_id = %s;
        """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, anime_id))

def check_movie_review_exists(user_id: int, movie_id: int) -> bool:
    query = """
    SELECT EXISTS (
        SELECT 1
        FROM movie_reviews
        WHERE user_id = %s AND movie_id = %s
    );
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, movie_id))
            return bool(cursor.fetchone()[0])


def check_series_review_exists(user_id: int, series_id: int) -> bool:
    query = """
    SELECT EXISTS (
        SELECT 1
        FROM series_reviews
        WHERE user_id = %s AND series_id = %s
    );
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, series_id))
            return bool(cursor.fetchone()[0])

def check_anime_review_exists(user_id: int, anime_id: int) -> bool:
    query = """
    SELECT EXISTS (
        SELECT 1
        FROM anime_reviews
        WHERE user_id = %s AND anime_id = %s
    );
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, anime_id))
            return bool(cursor.fetchone()[0])
