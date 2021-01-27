FROM python:3.7-slim

ENV MODEL_DIR=/api/model_exclude_wiki/word2vec.model

WORKDIR /api
COPY . /api
COPY model_exclude_wiki /api/model_exclude_wiki

RUN pip install Flask gunicorn gensim

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 main:app
