from python:3.8

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /

CMD ["python", "src/app.py"]
