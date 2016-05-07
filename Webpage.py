from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
  return render_template('welcome.html', title='Welcome', welcome_message='Greetings from the world of tomorrow')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

