FROM python:3.11.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ../requirements /app/
RUN pip install --upgrade pip
RUN pip install -r development.txt
COPY ../ /app/
