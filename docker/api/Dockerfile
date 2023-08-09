FROM python:3.8-slim

WORKDIR /project

COPY ./requirements.txt ./req.txt

COPY . .

RUN pip3 install -r req.txt

ENV PYTHONPATH "/project"

WORKDIR /project/app
CMD ["python3", "api.py"]