from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("Index.html")

@app.route('/Report')
def Report():
    lower_letter = False
    upper_letter = False
    num_end = False
    username = request.args.get('username')

    lower_letter = any(letter.islower() for letter in username)
    upper_letter = any(letter.isupper() for letter in username)
    num_end = username[-1].isdigit()

    report = lower_letter and upper_letter and num_end
    return render_template('Report.html',username = username,report = report,lower_letter=lower_letter,upper_letter=upper_letter,num_end=num_end)

if __name__ == '__main__':
    app.run(debug=True)
