from flask import Flask, render_template ,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return  render_template("homepage.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/page2')
def page2():
    return render_template("page2.html")

if( __name__ == '__main__'):
    app.run(host='0.0.0.0')
