import re
from tokenize import Number
from flask import Flask, redirect ,render_template, request , redirect,jsonify





app = Flask(__name__)



@app.route("/")
def html():
    
    return render_template("index.html")


@app.route("/",methods=['POST','GET'])
def reverse():
    c=request.form['reverse']
    b=int(c)
    rev=0
    tmp=b
    while(tmp>0):
        rev=rev*10+tmp%10
        tmp//=10
    result={
        "Number":b,
        "reverse":rev
    }
    return jsonify(result)

@app.route("/reverse/<int:a>",methods=['POST','GET'])
def reverseurl(a):
    rev=0
    tmp=a
    while(tmp>0):
        rev=rev*10+tmp%10
        tmp//=10
    result={
        "Number":a,
        "reverse":rev
    }
    return jsonify(result)





if __name__=="__main__":
    app.run(debug=True)
    