'''
You can't deliver an untested code, so here are some basic test for parser.
Let's make tests a spec-like, output of pytest-spec plugin makes it look
like RSpec or Mocha.
The coverage is minimal, but you've got an idea.
'''
import pytest
import os
from sgml_parser import parse as parse_sgml

FIXTURE = 'test_sgml_parser.fixture.sgm'


@pytest.fixture
def parsed_articles():
    fixture = os.path.join(os.path.dirname(__file__), FIXTURE)
    with open(fixture, 'r') as sgml:
        return parse_sgml(sgml)


def test_it_parsed_all_articles(parsed_articles):
    assert len(parsed_articles) == 2


def test_meta_tags_parsed_as_lists(parsed_articles):
    expected_places = ['el-salvador', 'usa', 'uruguay']
    assert parsed_articles[0]['meta']['places'] == expected_places


def test_each_article_has_a_structured_content(parsed_articles):
    for article in parsed_articles:
        assert 'text' in article
        assert 'body' in article['text']
        assert 'dateline' in article['text']
        assert 'title' in article['text']


def test_each_article_has_new_and_old_ids(parsed_articles):
    for article in parsed_articles:
        assert 'newid' in article
        assert 'oldid' in article
