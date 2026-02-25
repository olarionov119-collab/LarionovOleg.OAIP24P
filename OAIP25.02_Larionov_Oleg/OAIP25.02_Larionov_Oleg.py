from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/me')
def me():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '12345':
            return render_template('index.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)