FROM ubuntu:latest
  
COPY . .

ARG SECRET_KEY
ARG MYSQL_ROOT_PASSWORD
ARG MYSQL_DATABASE

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install flask_wtf
RUN pip3 install wtforms
RUN pip3 install flask-sqlalchemy
RUN pip3 install PyMySQL[rsa]

ENV SECRET_KEY=${SECRET_KEY}
ENV MYSQL_ROOT_PASSWORD=${DB_PASSWORD}
ENV MYSQL_DATABASE=fantasygendb

EXPOSE 5001

ENTRYPOINT ["python3", "service-two.py"]