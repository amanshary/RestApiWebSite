from flask import Flask
from flask import request
import logging
import os
import datetime

app = Flask(__name__)
@app.route("/")
def main():
    return "Welcome!"

def handlePost():
    logging.debug("Received post")
    logging.debug(request.form)
    return "handlePost"

def handleGet():
    logging.debug("Received get")
    logging.debug(request.form)
    return "handleGet"
@app.route('/myApp', methods=['GET', 'POST'])
def hello_name():
    if request.method == 'POST':
        return handlePost()
    elif request.method == 'GET':
        return handleGet()
    return ""

if __name__ == '__main__':
    if not os.path.exists("C:/temp/"):
        os.makedirs("C:/temp/")
    logging.basicConfig(filename="C:/temp/web.log",level=logging.DEBUG)
    logging.debug('Crawler is up: %s' % (datetime.datetime.now()))
    app.run()
    logging.debug('Crawler is down: %s' % (datetime.datetime.now()))