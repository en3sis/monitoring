
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from discord_webhook import DiscordEmbed, DiscordWebhook


def send_to_discord_webhook(json_data, url):
  print(f"Sending message to Discord webhook: {json_data}")

  system_name = os.uname().nodename

  title = json_data['title'] if 'title' in json_data else 'New message!'
  color = json_data['color'] if 'color' in json_data else '03b2f8'

  embed = DiscordEmbed(
      title=title, description=json_data['message'],
      color=color,
  )

  embed.set_footer(text='Sent from ' + system_name)

  webhook = DiscordWebhook(
      url=url)

  webhook.add_embed(embed)

  response = webhook.execute()

  print(f"Response from Discord webhook: {response}")


class MyServer(BaseHTTPRequestHandler):
  def do_POST(self):

    # Load the environment variables
    URL = os.environ['URL']
    SECRET = os.environ['SECRET']

    if self.headers.get('API-Key') == SECRET:
      content_length = int(self.headers['Content-Length'])
      post_data = self.rfile.read(content_length)
      json_data = json.loads(post_data)

      # Send the data to Discord
      send_to_discord_webhook(
          json_data,
          URL)

      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(b'Received POST request')
    else:
      self.send_response(401)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(b'Unauthorized')


def run(server_class=HTTPServer, handler_class=MyServer, port=8000):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f'Starting httpd on port {port}...')
  httpd.serve_forever()


if __name__ == '__main__':
  run()
