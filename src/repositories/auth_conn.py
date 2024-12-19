import psycopg2
from settings import DB_CONFIG
from hashlib import sha256

def hash_password(password: str) -> str:
    return sha256(password.encode('utf-8')).hexdigest()

def reg_new_user(username, email, role, password):
    hashed_password = hash_password(password) 
    query = """
        INSERT INTO users (username, email, password_hash, role)
        VALUES (%s, %s, %s, %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (username, email, hashed_password, role))

def check_new_user_login(username):
    query = "SELECT username FROM users WHERE username = %s;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (username,))
            row = cursor.fetchone()
            if row is None:
                return True  
            else:
                return False  


def check_new_user_email(email):
    query = "SELECT email FROM users WHERE email = %s;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            if row is None:
                return True  
            else:
                return False  

def check_auth_user(username, password) -> bool:
    hashed_password = hash_password(password)  
    query = "SELECT username, password_hash FROM users WHERE username = %s AND password_hash = %s;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (username, hashed_password))
            row = cursor.fetchone()
            if row is None:
                return True  
            else:
                return False 

def return_user_data(username, password):
    hashed_password = hash_password(password)  
    query = """
        SELECT user_id, username, email, role, created_at
        FROM users
        WHERE username = %s AND password_hash = %s;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (username, hashed_password))
            return cursor.fetchone()
        
