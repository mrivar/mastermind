FROM python:3.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./ /app
WORKDIR /app

RUN apt-get update && apt-get install -y build-essential nginx
COPY nginx.default /etc/nginx/sites-available/default
RUN make libs
RUN make migrations
RUN make collectstatic

RUN chown -R www-data:www-data /app
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD export PYTHONPATH=${PYTHONPATH}:/app && make run_gunicorn
