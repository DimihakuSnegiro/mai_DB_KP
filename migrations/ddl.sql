-- Создание таблицы пользователей с ролью
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'user')) -- Роль пользователя: admin или user
);

-- Создание таблицы фильмов
CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    release_year INT,
    duration INT, -- В минутах
    director VARCHAR(255),
    country VARCHAR(255),
    language VARCHAR(255),
    genre VARCHAR(255), -- Жанр
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание таблицы сериалов
CREATE TABLE series (
    series_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    release_year INT,
    number_of_seasons INT,
    number_of_episodes INT,
    creator VARCHAR(255),
    country VARCHAR(255),
    language VARCHAR(255),
    genre VARCHAR(255), -- Жанр сериала
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание таблицы аниме
CREATE TABLE anime (
    anime_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    release_year INT,
    number_of_episodes INT,
    studio VARCHAR(255),
    genre VARCHAR(255), -- Жанр аниме
    country VARCHAR(255), -- Страна производства
    language VARCHAR(255), -- Язык (обычно японский)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица рейтингов для фильмов
CREATE TABLE movie_ratings (
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    rating DECIMAL(3,1) DEFAULT 0,
    PRIMARY KEY (movie_id)
);

-- Таблица рейтингов для сериалов
CREATE TABLE series_ratings (
    series_id INT REFERENCES series(series_id) ON DELETE CASCADE,
    rating DECIMAL(3,1) DEFAULT 0,
    PRIMARY KEY (series_id)
);

-- Таблица рейтингов для аниме
CREATE TABLE anime_ratings (
    anime_id INT REFERENCES anime(anime_id) ON DELETE CASCADE,
    rating DECIMAL(3,1) DEFAULT 0,
    PRIMARY KEY (anime_id)
);

-- Таблица для оценок и комментариев для фильмов
CREATE TABLE movie_reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    rating DECIMAL(3,1),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для оценок и комментариев для сериалов
CREATE TABLE series_reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    series_id INT REFERENCES series(series_id) ON DELETE CASCADE,
    rating DECIMAL(3,1),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для оценок и комментариев для аниме
CREATE TABLE anime_reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    anime_id INT REFERENCES anime(anime_id) ON DELETE CASCADE,
    rating DECIMAL(3,1),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Функция для обновления рейтинга фильма
CREATE OR REPLACE FUNCTION update_movie_rating() RETURNS TRIGGER AS $$
BEGIN
    UPDATE movie_ratings
    SET rating = COALESCE((
        SELECT AVG(rating)
        FROM movie_reviews
        WHERE movie_id = COALESCE(NEW.movie_id, OLD.movie_id)
    ), 0)
    WHERE movie_id = COALESCE(NEW.movie_id, OLD.movie_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Функция для обновления рейтинга сериала
CREATE OR REPLACE FUNCTION update_series_rating() RETURNS TRIGGER AS $$
BEGIN
    UPDATE series_ratings
    SET rating = COALESCE((
        SELECT AVG(rating)
        FROM series_reviews
        WHERE series_id = COALESCE(NEW.series_id, OLD.series_id)
    ), 0)
    WHERE series_id = COALESCE(NEW.series_id, OLD.series_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Функция для обновления рейтинга аниме
CREATE OR REPLACE FUNCTION update_anime_rating() RETURNS TRIGGER AS $$
BEGIN
    UPDATE anime_ratings
    SET rating = COALESCE((
        SELECT AVG(rating)
        FROM anime_reviews
        WHERE anime_id = COALESCE(NEW.anime_id, OLD.anime_id)
    ), 0)
    WHERE anime_id = COALESCE(NEW.anime_id, OLD.anime_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Триггер для обновления рейтинга фильма после добавления/удаления/изменения отзыва
CREATE TRIGGER movie_rating_trigger
AFTER INSERT OR UPDATE OR DELETE ON movie_reviews
FOR EACH ROW
EXECUTE FUNCTION update_movie_rating();

-- Триггер для обновления рейтинга сериала после добавления/удаления/изменения отзыва
CREATE TRIGGER series_rating_trigger
AFTER INSERT OR UPDATE OR DELETE ON series_reviews
FOR EACH ROW
EXECUTE FUNCTION update_series_rating();

-- Триггер для обновления рейтинга аниме после добавления/удаления/изменения отзыва
CREATE TRIGGER anime_rating_trigger
AFTER INSERT OR UPDATE OR DELETE ON anime_reviews
FOR EACH ROW
EXECUTE FUNCTION update_anime_rating();

-- Функция для добавления записи в таблицу рейтингов для фильма
CREATE OR REPLACE FUNCTION add_movie_rating() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO movie_ratings (movie_id, rating)
    VALUES (NEW.movie_id, 0);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Функция для добавления записи в таблицу рейтингов для сериала
CREATE OR REPLACE FUNCTION add_series_rating() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO series_ratings (series_id, rating)
    VALUES (NEW.series_id, 0);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Функция для добавления записи в таблицу рейтингов для аниме
CREATE OR REPLACE FUNCTION add_anime_rating() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO anime_ratings (anime_id, rating)
    VALUES (NEW.anime_id, 0);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Триггер для добавления записи в таблицу movie_ratings после добавления фильма
CREATE TRIGGER add_movie_rating_trigger
AFTER INSERT ON movies
FOR EACH ROW
EXECUTE FUNCTION add_movie_rating();

-- Триггер для добавления записи в таблицу series_ratings после добавления сериала
CREATE TRIGGER add_series_rating_trigger
AFTER INSERT ON series
FOR EACH ROW
EXECUTE FUNCTION add_series_rating();

-- Триггер для добавления записи в таблицу anime_ratings после добавления аниме
CREATE TRIGGER add_anime_rating_trigger
AFTER INSERT ON anime
FOR EACH ROW
EXECUTE FUNCTION add_anime_rating();
