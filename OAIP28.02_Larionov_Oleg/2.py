from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<a>/<oper>/<b>/')

def index2(a,b,oper):
    a = float(a)
    b = float(b)

    return render_template('index2.html', a=a, b=b, oper=oper)

if __name__ == '__main__':
    app.run(debug=True)