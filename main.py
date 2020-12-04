from math import sqrt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print("Error: ", e)
        return "Hello world"

@app.route('/hello', methods=['POST'])
def params():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    sq = sqrt(b*b - 4*a*c)
    return (a,b,c)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)

print("Hello, welcome to quadratic solver")
a = request.form['a']
b = request.form['b']
c = request.form['c']
print(a, b, c)

sq = sqrt(b*b - 4*a*c)
print(eval("(%s - %s)/(2*%s)" % (-b, sq, a)))

def calculate(a, b, c):
    sq = sqrt(b*b - 4*a*c)
    result = lambda op: eval("(%s %s %s)/(2*%s)" % (-b, op, sq, a))
    return [result("-"), result("+")]

print("Your result is: "+str(calculate(a, b, c)[0])+", "+str(calculate(a, b, c)[1]))
