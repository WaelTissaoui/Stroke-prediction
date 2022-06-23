from flask import Flask,render_template,request
import pickle
import numpy as np
model = pickle.load(open(r"C:\\wamp64\\www\\dep\\xgbmodel.pkl","rb"))
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("from.html")
@app.route("/result",methods=["POST","GET"])
def result():
    output = request.args
    T = []
    for R,Z in output.items():
        print(R,Z)
        T.append(int(Z))
    T = np.array(T).reshape((1,-1))
    value = model.predict(T)
    if value == 0:
        link = "pass.png"
    else :
        link = "stroke1.png"


    print(value)
    return render_template("from.html",link = link , value = value )
if __name__ == '__main__':
    app.run(debug = True,port = 5001)