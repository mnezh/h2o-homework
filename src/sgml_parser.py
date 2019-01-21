# -*- coding: utf-8 -*-
"""
A relaxed Lewis SGML parser loosely based on specification in README.txt
Can tolerate some missing tags, such as BODY in TEXT
"""
from bs4 import BeautifulSoup
import dateparser


def parse(stream):
    return [
        parse_reuters_tag(reuters_tag)
        for reuters_tag
        in BeautifulSoup(stream, 'html.parser').find_all('reuters')
    ]


def parse_reuters_tag(reuters_tag):
    attributes = ['cgisplit', 'lewissplit', 'newid', 'topics', 'oldid']
    metas = ['companies', 'exchanges', 'orgs', 'people', 'places', 'topics']
    article = {'meta': {}}
    for attribute in attributes:
        article[attribute] = reuters_tag.get(attribute)
    for meta in metas:
        article['meta'][meta] = parse_d_list(reuters_tag.find(meta))
    article['text'] = parse_text_tag(reuters_tag.find('text'))
    article['meta']['date'] = parse_date(reuters_tag.date)
    article['raw'] = reuters_tag.prettify()
    return article


def parse_d_list(tag_with_d_list):
    return [d_tag.string for d_tag in tag_with_d_list.find_all('d')]


def inner_tag_or_empty(tag, inner_tag):
    inner = tag.find(inner_tag)
    return inner.string if inner else ''


def parse_text_tag(text_tag):
    return {
        'title': inner_tag_or_empty(text_tag, 'title').strip(),
        'dateline': inner_tag_or_empty(text_tag, 'dateline').strip(),
        'body': inner_tag_or_empty(text_tag, 'body')
    }


def parse_date(date_tag):
    return dateparser.parse(date_tag.string)
