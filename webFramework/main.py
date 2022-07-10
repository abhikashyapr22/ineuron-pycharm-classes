from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods = [ 'GET','POST'])
def homepage():
    return render_template('homepage.html')

@app.route('/sudh_function', methods=['POST'])
def url_test1():
    test1 = request.json['val1']
    test2 = request.json['val2']
    test3 = int(test1) + int(test2)
    return jsonify(test3)


if __name__ == '__main__':
    app.run()
