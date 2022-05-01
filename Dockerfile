FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

ENV BOT_TOKEN BOT_TOKEN

COPY main.py .

CMD ["python3", "main.py"]