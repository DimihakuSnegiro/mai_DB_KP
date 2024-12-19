import psycopg2
import pandas as pd
from psycopg2.extras import DictCursor
from settings import DB_CONFIG

def get_user_statistics(user_id):
    query = """
        SELECT
            (SELECT COUNT(*) FROM movie_reviews WHERE user_id = %s) AS movies_count,
            (SELECT COUNT(*) FROM series_reviews WHERE user_id = %s) AS series_count,
            (SELECT COUNT(*) FROM anime_reviews WHERE user_id = %s) AS anime_count;
    """
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (user_id, user_id, user_id))
                stats = cursor.fetchone()

        return {
            'movies_count': stats[0] if stats else 0,
            'series_count': stats[1] if stats else 0,
            'anime_count': stats[2] if stats else 0
        }
    except Exception as e:
        print(f"Error fetching user statistics: {e}")
        return {}

def get_user_reviews(user_id, category):
    if category == 'movies':
        query = """
            SELECT m.title AS "Title", r.rating AS "Rating", r.comment AS "Comment"
            FROM movie_reviews r
            JOIN movies m ON r.movie_id = m.movie_id
            WHERE r.user_id = %s;
        """
    elif category == 'series':
        query = """
            SELECT s.title AS "Title", r.rating AS "Rating", r.comment AS "Comment"
            FROM series_reviews r
            JOIN series s ON r.series_id = s.series_id
            WHERE r.user_id = %s;
        """
    elif category == 'anime':
        query = """
            SELECT a.title AS "Title", r.rating AS "Rating", r.comment AS "Comment"
            FROM anime_reviews r
            JOIN anime a ON r.anime_id = a.anime_id
            WHERE r.user_id = %s;
        """
    else:
        return pd.DataFrame(columns=["Title", "Rating", "Comment"])

    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (user_id,))
                reviews = cursor.fetchall()

        if reviews:
            return pd.DataFrame(reviews, columns=["Title", "Rating", "Comment"])
        else:
            return pd.DataFrame(columns=["Title", "Rating", "Comment"])

    except Exception as e:
        print(f"Error fetching user reviews: {e}")
        return pd.DataFrame(columns=["Title", "Rating", "Comment"])

def get_user_info(user_id):
    query = """
        SELECT username, email, role, to_char(created_at, 'YYYY-MM-DD HH24:MI') AS created_at
        FROM users 
        WHERE user_id = %s;
    """
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (user_id,))
                user_info = cursor.fetchone()

        if user_info:
            return {
                'username': user_info[0],
                'email': user_info[1],
                'role': user_info[2],
                'created_at': user_info[3]
            }
        return None
    except Exception as e:
        print(f"Error fetching user info: {e}")
        return None
