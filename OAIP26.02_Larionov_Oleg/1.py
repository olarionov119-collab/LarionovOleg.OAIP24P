from flask import Flask, render_template, request
from random import random

app = Flask(__name__)

@app.route('/<float:num>')
def index(num):

    number = num * 2

    text = f"Ваше число {num}, умноженное на 2: {number}"

    return render_template('index.html',
                           number=number,
                           text=text)
if __name__ == '__main__':
    app.run(debug=True)