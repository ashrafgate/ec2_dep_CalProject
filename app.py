#pip install flask
from flask import Flask, render_template
import calendar
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
#if __name__== '__main__':
    #app.run(debug=True)

if __name__== '__main__':
    app.run(debug=True, port=8080)
