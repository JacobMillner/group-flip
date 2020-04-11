FROM python:3.7

WORKDIR /server

RUN apt-get update

COPY . .

RUN ["chmod", "+x", "./server_setup.sh"]
RUN ["./server_setup.sh"]

CMD ["python","-u","/server/src/server.py"]