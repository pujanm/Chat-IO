FROM ubuntu:16.04

WORKDIR /usr/chat_source

COPY . .

RUN apt-get update && apt-get upgrade -y && \
    apt-get install redis-server -y && \
    apt-get install python3 -y && apt-get install python3-pip -y && \
    pip3 install --no-cache-dir -r requirements.txt && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    chmod a+x entrypoint.sh

EXPOSE 8000

CMD ["sh", "-c", "./entrypoint.sh"]