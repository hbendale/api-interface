FROM python:3.10.4-alpine3.15 as dev

WORKDIR /work

COPY requirements.txt /work/requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

ENV PYTHONPATH=/work

COPY ./src/ /work/src

FROM dev as runtime

ENV PYTHONPATH=/app

COPY ./src/ /app/src

ENTRYPOINT ["python", "/app/src/main.py"]