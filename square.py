from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def square():
    if request.method == "POST":
        if(request.form['num']) == '':
            return "invalid input"
        else:
            no = request.form['num']
            sq = int(no)*int(no)
            return render_template('answer.html',squared = sq,num =no)
    if request.method == "GET":
        return render_template("square.html")
if __name__ == "__main__":
    app.run(debug=True)