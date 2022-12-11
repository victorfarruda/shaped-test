FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN python manage.py migrate
CMD python manage.py runserver 8500
