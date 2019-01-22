'''
Article query service, runs on a top of SGML data converted to JSON.
Dates from JSON are converted to datetime objects.
'''
import json
import dateparser
from pydash import get as get_nested
from schema import attributes, metas, fulltext


class Articles:
    date_queries = {
        'date': '%Y-%m-%d',
        'day': '%-d',
        'month': '%-m',
        'year': '%Y'
    }

    def __init__(self, file_name):
        self.matchers = Articles.build_matchers()
        with open(file_name) as input:
            self.articles = json.load(input)
        for article in self.articles:
            article['meta']['date'] = dateparser.parse(article['meta']['date'])

    def find_all(self, query={}):
        return [
            article
            for article
            in self.articles
            if self.article_matches(article, query)
        ]

    def find_first(self, query={}):
        return next((
            article
            for article
            in self.articles
            if self.article_matches(article, query)
        ), None)

    def article_matches(self, article, query):
        for key in query:
            value = query[key]
            if key in Articles.date_queries and not Articles.match_date(
                    article, key, value):
                return False
            else:
                matcher = self.matchers.get(key, None)
                if matcher and not matcher(get_nested(article, key), value):
                    return False
        return True

    @staticmethod
    def build_matchers():
        matchers = {}
        containers = Articles.add_prefix(
            fulltext, 'text') + Articles.add_prefix(metas, 'meta')
        for attribute in attributes:
            matchers[attribute] = Articles.equal_matcher
        for container in containers:
            matchers[container] = Articles.contains_matcher
        return matchers

    @staticmethod
    def match_date(article, date_part, value):
        return article['meta']['date'].strftime(
            Articles.date_queries[date_part]) == value

    @staticmethod
    def add_prefix(str_list, prefix):
        return ['%s.%s' % (prefix, string) for string in str_list]

    @staticmethod
    def equal_matcher(val1, val2):
        return val1 == val2

    @staticmethod
    def contains_matcher(container, comma_separated_values):
        for value in comma_separated_values.split(','):
            if value not in container:
                return False
        return True
