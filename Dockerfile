FROM ubuntu:20.04

WORKDIR /app

RUN apt update -y

RUN apt install unzip curl sudo -y

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

RUN useradd -m seed && echo "seed:seed" | chpasswd && adduser seed sudo

RUN curl -o src-cloud.zip https://seed.nyc3.cdn.digitaloceanspaces.com/src-cloud.zip

RUN unzip src-cloud.zip
