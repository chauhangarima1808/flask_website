from flask import Flask, send_from_directory

app = Flask(__name__)

import webserver.views
app.run(host='192.168.1.83',port=8765)


