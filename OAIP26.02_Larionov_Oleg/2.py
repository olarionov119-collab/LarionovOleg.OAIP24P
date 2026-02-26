from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<float:r>')
def index(r):

    pi = 3.14

    text = f"Площадь круга с радиусом {r} равна {pi*(r**2)}"

    return render_template('index.html',
                           r=r,
                           pi=pi,
                           text=text)

if __name__ == '__main__':
    app.run(debug=True)