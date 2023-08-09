FROM debian:buster

WORKDIR /project

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y libreoffice && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["libreoffice", "--headless"]