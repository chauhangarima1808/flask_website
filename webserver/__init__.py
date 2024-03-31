from flask import Flask, send_from_directory

app = Flask(__name__)

import webserver.views
app.run(port=8000)
