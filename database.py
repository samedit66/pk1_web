from article import Article


class Database:
    articles = []

    @staticmethod
    def save(article: Article):
        Database.articles.append(article)

    @staticmethod
    def find_article_by_title(title):
        for article in Database.articles:
            if article.title == title:
                return article
        return None

    @staticmethod
    def get_all_articles():
        return Database.articles
