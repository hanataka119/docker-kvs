import flask
app = flask.Flask('app server')

@app.route('/')
def index():
  return 'hanataka119 Hello Docker'

app.run(debug=True, host='0.0.0.0', port=80)