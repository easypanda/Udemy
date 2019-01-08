from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello Puppy!</h1>'

@app.route('/information')
def info():
    return "<h1> Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "Upper case: {}".format(name.upper())

if __name__ == '__main__':
    app.run()
