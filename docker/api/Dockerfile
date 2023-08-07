FROM python:3.8-slim

WORKDIR /project

COPY ./requirements.txt ./req.txt

RUN pip3 install -r req.txt

ENV PYTHONPATH "/project"

WORKDIR app
CMD ["python3", "api.py"]