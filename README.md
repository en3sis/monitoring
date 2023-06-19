# Monitoring tool

Generic tool that receives a request and sends a message to a discord webhook channel.

## Run container

```bash
docker build -t monitoring:latest .

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
	"message": "this is a bad error! =/"
}'
```
