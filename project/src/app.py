from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')


def hello_method():
    return render_template('home.html')


@app.route('/Home')
def home_method():
    return render_template('home.html')


app.route('/Services')
def services_method():
    return render_template('services.html')


@app.route('/About')
def about_method():
    return render_template('about.html')


@app.route('/base')
def base_method():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=5000)