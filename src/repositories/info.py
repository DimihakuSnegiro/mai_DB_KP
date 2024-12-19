import psycopg2
from psycopg2.extras import DictCursor
from settings import DB_CONFIG

def fetch_movie_info(title):
    query = """
        SELECT title, description, release_year, duration, director, country, language, genre
        FROM movies
        WHERE title = %s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (title,))
            return cur.fetchone()


def fetch_series_info(title):
    query = """
        SELECT title, description, release_year, number_of_seasons, number_of_episodes, creator, country, language, genre
        FROM series
        WHERE title = %s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (title,))
            return cur.fetchone()


def fetch_anime_info(title):
    query = """
        SELECT title, description, release_year, number_of_episodes, studio, genre, country, language
        FROM anime
        WHERE title = %s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (title,))
            return cur.fetchone()

def fetch_reviews(category, title):
    table_map = {
        'Movies': 'movie_reviews',
        'Series': 'series_reviews',
        'Anime': 'anime_reviews'
    }

    foreign_key_map = {
        'Movies': 'movie_id',
        'Series': 'series_id',
        'Anime': 'anime_id'
    }

    category_table_map = {
        'Movies': 'movies',
        'Series': 'series',
        'Anime': 'anime'
    }

    category = category.capitalize()


    if category not in table_map:
        raise ValueError(f"Unknown category: {category}")

    category_table = table_map[category]
    foreign_key = foreign_key_map[category]
    category_table_content = category_table_map[category]

    category_lower = category.lower()

    query = f"""
        SELECT u.username, r.rating, r.comment
        FROM {category_table} r
        JOIN users u ON r.user_id = u.user_id
        JOIN {category_table_content} m ON r.{foreign_key} = m.{category_lower}_id
        WHERE m.title = %s
    """

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (title,))
            rows = cur.fetchall()
            return rows
