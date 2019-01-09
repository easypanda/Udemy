from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    mylist = [1,2,3,4,5]
    return render_template('basic.html',mylist=mylist)

if __name__ == '__main__':
    app.run(debug=True)
