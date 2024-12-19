import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

def get_id_movie(name) -> int:
    query = """
        SELECT movie_id
        FROM movies
        WHERE title = %s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name,))
            result = cursor.fetchone()
            return result[0] if result else None
        
def get_id_anime(name) -> int:
    query = """
        SELECT anime_id
        FROM anime
        WHERE title = %s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name,))
            result = cursor.fetchone()
            return result[0] if result else None
        
def get_id_series(name) -> int:
    query = """
        SELECT series_id
        FROM series
        WHERE title = %s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name,))
            result = cursor.fetchone()
            return result[0] if result else None
        
def movie_exist(name) -> bool:
    movie_id = get_id_movie(name)
    if movie_id is None:
        return False
    else:
        return True
    
def anime_exist(name) -> bool:
    movie_id = get_id_anime(name)
    if movie_id is None:
        return False
    else:
        return True
    
def series_exist(name) -> bool:
    movie_id = get_id_anime(name)
    if movie_id is None:
        return False
    else:
        return True