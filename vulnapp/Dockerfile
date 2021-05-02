#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
#RUN apk --update add bash nano
#ENV STATIC_URL /static
#ENV STATIC_PATH /var/www/app/static
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt

FROM python:3.9.4-alpine3.13

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
