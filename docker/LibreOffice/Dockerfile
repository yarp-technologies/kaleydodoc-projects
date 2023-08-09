FROM ubuntu:20.04

ENV TZ=Europe/Paris

RUN apt-get update && \
    apt-get install -y libreoffice && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["libreoffice"]