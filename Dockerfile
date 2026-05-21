FROM python:3.12-alpine

RUN apk --no-cache add curl

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5500

COPY . .

CMD [ "python3", "server.py" ]