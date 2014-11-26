FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y git
RUN apt-get install -y python-pip

COPY . /var/paz-fit2

RUN pip install -r /var/paz-fit2/requirements.txt 

ENTRYPOINT ["python","/var/paz-fit2/src/app.py"]

EXPOSE 5000
