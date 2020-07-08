FROM ubuntu:latest
  
COPY . .

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install flask_wtf
RUN pip3 install wtforms

EXPOSE 5002

ENTRYPOINT ["python3", "service-three.py"]