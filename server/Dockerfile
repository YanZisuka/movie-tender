FROM python:3.9.13

ENV PYTHONUNBUFFERED=0

RUN   apt-get update && apt-get -y install libpq-dev

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]
EXPOSE 8000

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /