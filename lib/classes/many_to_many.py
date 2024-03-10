class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        if len(name) == 0:
            raise Exception("Author name cannot be empty")
        self._name = name
        self._articles = []
        self._magazines = []

    def articles(self):
        return self._articles

    def magazines(self):
        return self._magazines

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        if article.magazine not in self._magazines:
            self._magazines.append(article.magazine)
        self._articles.append(article)
        return article

    def topic_areas(self):
        pass
    
    @property
    def name(self):
        return self._name

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

    # pytest lib/testing/author_test.py -x