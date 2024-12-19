import psycopg2
import psycopg2.extras
from settings import DB_CONFIG
import pandas as pd

def get_media_data(category: str) -> pd.DataFrame:
    if category == "Movies":
        query = """
        SELECT m.title, m.genre, mr.rating
        FROM movies m
        JOIN movie_ratings mr ON m.movie_id = mr.movie_id
        """
    elif category == "Series":
        query = """
        SELECT s.title, s.genre, sr.rating
        FROM series s
        JOIN series_ratings sr ON s.series_id = sr.series_id
        """
    elif category == "Anime":
        query = """
        SELECT a.title, a.genre, ar.rating
        FROM anime a
        JOIN anime_ratings ar ON a.anime_id = ar.anime_id
        """
    else:
        return pd.DataFrame()

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return pd.DataFrame(cursor.fetchall(), columns=["title", "genre", "average_rating"])