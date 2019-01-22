#!/usr/bin/env python
'''
A smallest possible transport layer on a top of article query service.
Handles JSON serialization of datetime correcly.
'''
import os
import sys
from flask import Flask, request, jsonify, make_response
from serialize_datetime import CustomJSONEncoder
from articles import Articles

DEFAULT_DATA = '../data/reut2-000.json'
json_file = sys.argv[1] if len(
    sys.argv) > 1 else os.path.join(
        os.path.dirname(__file__), DEFAULT_DATA)
articles = Articles(json_file)
app = Flask('Reuters API')
app.json_encoder = CustomJSONEncoder


@app.route("/article", methods=["GET"])
@app.route('/article/<new_id>')
def get_article(new_id=None):
    if new_id:
        article = articles.find_first({'newid': new_id})
        if article:
            return jsonify(article)
        return make_response(jsonify({'error': 'Not found'}), 404)
    else:
        return jsonify(articles.find_all(request.args))


if __name__ == '__main__':
    app.run(debug=True, port=9666)
