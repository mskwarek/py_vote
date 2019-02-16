FROM python:3.6-slim

COPY requirements.txt /deps/requirements.txt

VOLUME /app/backend
WORKDIR /app/backend

RUN pip install -r /deps/requirements.txt
EXPOSE 5000

CMD python3 /app/backend/serve.py