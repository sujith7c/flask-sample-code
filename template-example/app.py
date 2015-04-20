#!/usr/bin/python
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def tida():
  para = {'div1':"Lopes",'div2':"dfasfas"}
  return render_template('index.html',content=para)

if __name__ == '__main__':
 app.run(debug=True)


