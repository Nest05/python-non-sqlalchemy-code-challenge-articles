class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters long.")

        self._author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

        
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
        if article not in self._articles:
            self._articles.append(article)
        if article.magazine not in self._magazines:
            self._magazines.append(article.magazine)

        magazine.add_article(article)
        return article

    def topic_areas(self):
        topics = set()
        for article in self._articles:
            topics.add(article.magazine.name)
        if len(topics) == 0:
            return None
        else:
            return list(topics)
    
    @property
    def name(self):
        return self._name

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise Exception("Names must be of type str and between 2 and 16 characters, inclusive")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise Exception("Categories must be of type str and longer than 0 characters")
   
    def add_article(self, article):
        self._articles.append(article)
        
    def articles(self):
        return self._articles
    
    @property
    def contributors(self):
        return list(self._contributors)

    def article_titles(self):
        if len(self._articles) > 0:
            return [article.title for article in self._articles]
        else:
            return None

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author
            if author in authors_count:
                authors_count[author] += 1
            else:
                authors_count[author] = 1

        contributing_authors = [author for author, count in authors_count.items() if count > 2]

        if len(contributing_authors) > 0:
            return contributing_authors
        else:
            return None

    def publish_article(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
            self._contributors.add(article.author)
        else:
            raise Exception("Articles must be of type Article")
    




    # pytest lib/testing/author_test.py -x
    # pytest lib/testing/magazine_test.py -x
    # pytest lib/testing/article_test.py -x