FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache ffmpeg \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python3 -u ./bot.py"]    