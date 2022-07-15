from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/operation', methods=['POST','GET'])
def url_test1():
    val1 = request.json['val1']
    val2 = request.json['val2']
    result = int(val1) + int(val2)
    return ''''''


if __name__ == '__main__':
    app.run()
