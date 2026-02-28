from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<a>/<b>/<c>/')

def index(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    return render_template('index1.html', a=a, b=b, c=c)

if __name__ == '__main__':
    app.run(debug=True)