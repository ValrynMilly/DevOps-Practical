FROM ubuntu:latest
  
COPY . .

ARG SECRET_KEY

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

EXPOSE 5003

ENTRYPOINT ["python3", "service-four.py"]