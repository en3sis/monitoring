# Notification tool

A generic tool that receives a request and sends a message to a discord webhook channel.

## Run container


You can run the container with the following command:

```bash
docker run -e URL="DISCORD_WEBHOOK_URL" -e SECRET="YOUR_SECRET_TOKEN" -p 8000:8000 --name monitoring en3sis/monitoring:latest
```
```

or, you can build the image and run it:
```bash
docker build -t zypherus:latest .

docker run -e URL="DISCORD_WEBHOOK_URL" -e SECRET="YOUR_SECRET_TOKEN" -p 8000:8000 --name monitoring monitoring:latest
```

## Request example

```bash
curl --request POST \
  --url http://localhost:8000/ \
  --header 'API-Key: SECRET' \
  --header 'Content-Type: application/json' \
  --data '{
	"type": "error",
  "color": "0ff0000",
	"message": "This is a bad error! =/"
}'
```
