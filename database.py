import sqlite3

from article import Article


class Database:
    articles = []

    DATABASE = "database.db"
    SCHEMA = "schema.sql"

    @staticmethod
    def execute(sql, params=()):
        # 1. Подключаемся к базе данных
        connection = sqlite3.connect(Database.DATABASE)

        # 2. Получаем курсор базы данных
        cursor = connection.cursor()

        # 3. Ввыполняем какой-то код...
        cursor.execute(sql, params)

        # 4. Фиксируем изменения в БД
        connection.commit()

    @staticmethod
    def create_table():
        with open(Database.SCHEMA) as schema_file:
            Database.execute(schema_file.read())

    @staticmethod
    def save(article: Article):
        if Database.find_article_by_title(article.title) is not None:
            return False

        Database.execute(
            "INSERT INTO articles VALUES (?, ?, ?)",
            [article.title, article.content, article.photo]
        )
        return True

    @staticmethod
    def find_article_by_title(title):
        # 1. Подключаемся к базе данных
        connection = sqlite3.connect(Database.DATABASE)

        # 2. Получаем курсор базы данных
        cursor = connection.cursor()

        # 3. Ищем заданную статью
        cursor.execute("SELECT * FROM articles WHERE title = ?", [title])
        articles = cursor.fetchall()

        if len(articles) == 0:
            return None

        """
        article[0] == (12312, "Соник", "Соник это еж", "sonic.png")
        """

        article = Article(
            articles[0][0],
            articles[0][1],
            articles[0][2],
            articles[0][3]
        )
        return article

    @staticmethod
    def get_all_articles():
        return Database.articles
