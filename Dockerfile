FROM circleci/python:2.7.15
WORKDIR /app
RUN sudo chown circleci /app
COPY src/ /app
COPY Pipfile* /app/
COPY raw_data/reut2-000.sgm /app
RUN cd /app && pipenv install
RUN cd /app && pipenv run ./sgml2json.py /app/reut2-000.sgm /app/reut2-000.json
EXPOSE 9666
CMD cd /app && pipenv run ./app.py /app/reut2-000.json
