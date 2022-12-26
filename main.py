#https://flask.palletsprojects.com/en/1.1.x/quickstart/
from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/sumoftwonumbers/')
def sum():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    sum=a+b
    result={"number": [a,b],
            "Result": sum}
    return jsonify(result)

if __name__=="__main__":
    app.run()