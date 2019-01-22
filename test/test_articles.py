import dateparser
import os
import pytest
from articles import Articles


FIXTURE = 'test_articles.fixture.json'


@pytest.fixture
def loaded_articles():
    fixture = os.path.join(os.path.dirname(__file__), FIXTURE)
    return Articles(fixture)


# covers requirement:
# 1. API to list content
def test_it_lists_all_articles(loaded_articles):
    assert len(loaded_articles.find_all()) == 3


# covers requirement:
# 3. API get a specific content by id/any identifier
def test_it_fetches_article_by_id(loaded_articles):
    assert loaded_articles.find_first({'newid': '1'})['newid'] == '1'


# the rest cover requirement:
# 2. API to search content
def test_it_filters_articles_by_one_person(loaded_articles):
    articles = loaded_articles.find_all({'meta.people': 'dude1'})
    for article in articles:
        print(article['meta'])
        assert 'dude1' in article['meta']['people']


def test_it_filters_articles_by_multiple_persons(loaded_articles):
    people = 'dude1,dude2'
    articles = loaded_articles.find_all({'meta.people': people})
    for article in articles:
        for person in people.split(','):
            assert person in article['meta']['people']


def test_it_filters_articles_by_date(loaded_articles):
    date = '1987-02-26'
    articles = loaded_articles.find_all({'date': date})
    for article in articles:
        assert article['meta']['date'].date() == dateparser.parse(date).date()


def test_it_filters_articles_by_date_part(loaded_articles):
    year = '1987'
    articles = loaded_articles.find_all({'year': year})
    for article in articles:
        assert str(article['meta']['date'].date().year) == year


def test_it_filters_articles_by_fulltext_fields(loaded_articles):
    phrase = 'said it filed'
    articles = loaded_articles.find_all({'text.body': phrase})
    for article in articles:
        assert phrase in article['text']['body']


def test_it_can_combine_filters(loaded_articles):
    phrase = 'said'
    year = '1987'
    articles = loaded_articles.find_all({'text.body': phrase, 'year': year})
    for article in articles:
        assert phrase in article['text']['body']
        assert str(article['meta']['date'].date().year) == year
