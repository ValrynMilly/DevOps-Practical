FROM ubuntu:latest
  
COPY . .

ARG SECRET_KEY
ARG SQLALCHEMY_DATABASE_URI

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
ENV SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}

EXPOSE 5002

ENTRYPOINT ["python3", "service-three.py"]