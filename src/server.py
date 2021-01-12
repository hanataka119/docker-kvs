import flask, os, re, redis
from random import randint

COLOR = f'rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})'
HTML = '''<!DOCTYPE html>
<html><body style="background-color:{}">
  <h1>Version:1, HostName:{}</h1>
</body><html>'''

app = flask.Flask('app server')
@app.route('/', methods=['GET'])
def index():

  return HTML.format(COLOR, os.uname()[1])

app.run(debug=True, host='0.0.0.0', port=80)