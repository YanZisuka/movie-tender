FROM python:3.9.13
ENV PYTHONUNBUFFERED 1
WORKDIR /server
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0:8000"]
EXPOSE 8000
