FROM python:3.9.13

RUN apt-get update
RUN apt-get install -y net-tools
RUN apt-get install -y dnsutils
RUN apt-get update

ENV PYTHONUNBUFFERED 1

WORKDIR /home/server/

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]
EXPOSE 8000

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /