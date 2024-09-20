FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache ffmpeg \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python /app/bot.py"]    