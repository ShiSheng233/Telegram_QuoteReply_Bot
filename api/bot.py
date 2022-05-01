import json
import os
import sys
from http.server import BaseHTTPRequestHandler

import telegram
import telegram.ext
from cowpy import cow

sys.path.append("..")
from main import reply_to_message

bot = telegram.Bot(os.environ.get("BOT_TOKEN"))


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        reply_to_message(
            telegram.Update.de_json(json.loads(self.rfile.read(int(self.headers['content-length'])).decode()), bot),
            None,
        )

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello world!')
        self.wfile.write(message.encode())
        return
