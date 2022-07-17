from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/operation', methods=['POST'])
def url_test1():
    if request.method == 'POST':
        val1 = request.form.get('Value1', 0)
        val2 = request.form.get('Value2', 0)
        result = int(val1) + int(val2)
        #return f"Result is {result}"

        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run()
