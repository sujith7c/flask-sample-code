#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def tida():
  return '<h1>Hi all</h1>'

if __name__ == '__main__':
 app.run(debug=True)


