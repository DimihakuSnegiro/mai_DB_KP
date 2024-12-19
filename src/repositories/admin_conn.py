from pandas import DataFrame
import psycopg2
from settings import DB_CONFIG

def get_all_movies() -> DataFrame:
    """Получает список всех фильмов с их ID."""
    query = """SELECT movie_id, title FROM movies"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=['Movie_ID', 'Title'])

def get_all_series() -> DataFrame:
    """Получает список всех сериалов с их ID."""
    query = """SELECT series_id, title FROM series"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=['Series_ID', 'Title'])

def get_all_anime() -> DataFrame:
    """Получает список всех аниме с их ID."""
    query = """SELECT anime_id, title FROM anime"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=['Anime_ID', 'Title'])

def get_all_non_admin_users() -> DataFrame:
    """Получает список ID всех пользователей, которые не являются администраторами."""
    query = """SELECT user_id, username FROM users WHERE role != 'admin'"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=['User_ID', 'Username'])

def get_movie_ratings(movie_id: int) -> DataFrame:
    """Получает все оценки на фильм по его ID."""
    query = """SELECT u.username, r.rating, r.comment
               FROM movie_reviews r 
               JOIN users u ON u.user_id = r.user_id 
               WHERE r.movie_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (movie_id,))
            return DataFrame(cursor.fetchall(), columns=['Username', 'Rating', 'Comment'])

def get_series_ratings(series_id: int) -> DataFrame:
    """Получает все оценки на сериал по его ID."""
    query = """SELECT u.username, r.rating, r.comment
               FROM series_reviews r 
               JOIN users u ON u.user_id = r.user_id 
               WHERE r.series_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (series_id,))
            return DataFrame(cursor.fetchall(), columns=['Username', 'Rating', 'Comment'])

def get_anime_ratings(anime_id: int) -> DataFrame:
    """Получает все оценки на аниме по его ID."""
    query = """SELECT u.username, r.rating, r.comment
               FROM anime_reviews r 
               JOIN users u ON u.user_id = r.user_id 
               WHERE r.anime_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (anime_id,))
            return DataFrame(cursor.fetchall(), columns=['Username', 'Rating', 'Comment'])

def movie_rating_exists(movie_id: int) -> bool:
    """Проверяет, существует ли оценка для фильма по его ID."""
    query = """SELECT 1 FROM movie_ratings WHERE movie_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (movie_id,))
            return cursor.fetchone() is not None

def series_rating_exists(series_id: int) -> bool:
    """Проверяет, существует ли оценка для сериала по его ID."""
    query = """SELECT 1 FROM series_ratings WHERE series_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (series_id,))
            return cursor.fetchone() is not None

def anime_rating_exists(anime_id: int) -> bool:
    """Проверяет, существует ли оценка для аниме по его ID."""
    query = """SELECT 1 FROM anime_ratings WHERE anime_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (anime_id,))
            return cursor.fetchone() is not None
        
def user_exists(user_id: int) -> bool:
    """Проверяет, существует ли пользователь с заданным user_id."""
    query = """SELECT 1 FROM users WHERE user_id = %s"""
    
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id,))
            return cursor.fetchone() is not None
        
def get_movie_ratings_by_user(user_id: int) -> DataFrame:
    """Получает все оценки пользователя на фильмы по его ID."""
    query = """SELECT r.review_id, r.movie_id, m.title, r.rating, r.comment
               FROM movie_reviews r
               JOIN movies m ON r.movie_id = m.movie_id
               WHERE r.user_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id,))
            return DataFrame(cursor.fetchall(), columns=['Review_ID', 'Movie_ID', 'Title', 'Rating', 'Comment'])

def get_series_ratings_by_user(user_id: int) -> DataFrame:
    """Получает все оценки пользователя на сериалы по его ID."""
    query = """SELECT r.review_id, r.series_id, s.title, r.rating, r.comment
               FROM series_reviews r
               JOIN series s ON r.series_id = s.series_id
               WHERE r.user_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id,))
            return DataFrame(cursor.fetchall(), columns=['Review_ID', 'Series_ID', 'Title', 'Rating', 'Comment'])

def get_anime_ratings_by_user(user_id: int) -> DataFrame:
    """Получает все оценки пользователя на аниме по его ID."""
    query = """SELECT r.review_id, r.anime_id, a.title, r.rating, r.comment
               FROM anime_reviews r
               JOIN anime a ON r.anime_id = a.anime_id
               WHERE r.user_id = %s"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id,))
            return DataFrame(cursor.fetchall(), columns=['Review_ID', 'Anime_ID', 'Title', 'Rating', 'Comment'])

def is_admin(user_id):
    query = """
            SELECT role FROM users WHERE user_id = %s;
        """
    
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            
            if result:
                return result[0] == 'admin'
            else:
                return False
            
def check_anime_review_exists(review_id):
    query = """
        SELECT EXISTS(SELECT 1 FROM anime_reviews WHERE review_id = %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (review_id,))
            result = cursor.fetchone()
    
    return result[0]  

def check_movie_review_exists(review_id):
    query = """
        SELECT EXISTS(SELECT 1 FROM movie_reviews WHERE review_id = %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (review_id,))
            result = cursor.fetchone()
    
    return result[0]  

def check_series_review_exists(review_id):
    query = """
        SELECT EXISTS(SELECT 1 FROM series_reviews WHERE review_id = %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (review_id,))
            result = cursor.fetchone()
    
    return result[0]

def delete_anime_review(review_id):
    query_delete_review = """
        DELETE FROM anime_reviews WHERE review_id = %s;
    """
    
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query_delete_review, (review_id,))


def delete_movie_review(review_id):
    query_delete_review = """
        DELETE FROM movie_reviews WHERE review_id = %s;
    """
    
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query_delete_review, (review_id,))

def delete_series_review(review_id):
    query_delete_review = """
        DELETE FROM series_reviews WHERE review_id = %s;
    """
    
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query_delete_review, (review_id,))