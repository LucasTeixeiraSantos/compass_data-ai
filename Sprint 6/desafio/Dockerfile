FROM python:3.11-slim

WORKDIR /app

COPY data/ /app/data/

COPY script.py /app/script.py

RUN pip install boto3

RUN ls -l /app/data/

CMD ["python", "/app/script.py"]
