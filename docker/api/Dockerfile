FROM python:3.8-slim

WORKDIR /project

COPY ./requirements.txt ./req.txt

COPY . .

RUN echo deb http://ftp.ru.debian.org/debian/ jessie main non-free contrib >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y \
    libreoffice-writer \
    openjdk-7-jre-headless \
    ttf-mscorefonts-installer \
    && pip install aiohttp \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r req.txt

ENV PYTHONPATH "/project"

WORKDIR /project/app
CMD ["python3", "api.py"]