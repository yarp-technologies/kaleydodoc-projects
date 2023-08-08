FROM python:3.8-slim

WORKDIR /project

COPY ./requirements.txt ./req.txt

COPY . .

RUN apt-get update && apt-get -y install \
    unoconv \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r req.txt

ENV PYTHONPATH "/project"

WORKDIR /project/app
CMD ["python3", "api.py"]