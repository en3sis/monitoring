FROM alpine:latest
WORKDIR /app

COPY requirements.txt /app
COPY main.py /app

# Install dependecies
RUN apk add --no-cache python3 py3-pip
RUN pip3 install -r requirements.txt

EXPOSE 8000:8000

CMD ["python3", "/app/main.py"]
