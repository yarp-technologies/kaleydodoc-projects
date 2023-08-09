FROM python:3.8-slim

WORKDIR /project

RUN apt-get update && apt-get install -y docker-compose

COPY ./requirements.txt ./req.txt

COPY . .

RUN pip3 install -r req.txt

ENV PYTHONPATH "/project"

WORKDIR /project
CMD ["python3", "api.py"]