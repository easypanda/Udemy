from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

@app.route("/puppy_latin/<name>")
def puppy_latin(name):
    if name[-1] != "y":
        return "<h1> Hi {}! Your puppylatin name is {}y </h1>".format(name,name)
    return "<h1> Hi {}! Your puppylatin name is {}iful </h1>".format(name,name[:-1])

if __name__ == '__main__':
    app.run(debug=True)

#A cleaner way to do it is:
# if name[-1] == "y":
#   name = name[:-1]+"iful"
# else:
#   name = name + "y"
