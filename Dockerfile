FROM python:3

WORKDIR /usr/webapp

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./webapp/app.py app.py

EXPOSE 5000

CMD [ "python", "app.py" ]


# docker-compose ps -a 
# docker-compose down 
# docker ps -a 
# docker rm $(docker ps -aq)
# docker rmi $(docker images -aq)

# docker build .
# docker-compose up --build 