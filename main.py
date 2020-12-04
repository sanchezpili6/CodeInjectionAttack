from math import sqrt
from flask import Flask, render_template, request
import unicodedata

app = Flask(__name__)

def calculate(a, b, c):
    result = lambda op: eval("(1/(2*%s))*(%s %s %s)" % (a, -float(b), op, getSqrt(b, a, c)))
    print(result("-"))
    return [result("-"), result("+")]

def getSqrt(b, a, c):
    try:
        return sqrt(b*b - 4*a*c)
    except:
        return "None"

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print("Error: ", e)
        return "Hello world"

@app.route('/params', methods=['POST'])
def params():
    a = str(request.form['a']).strip('u').strip('\'')
    b = str(request.form['b']).strip('u').strip('\'')
    c = str(request.form['c']).strip('u').strip('\'')
    return "Your result is: "+str(calculate(a, b, c)[0])+", "+str(calculate(a, b, c)[1])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)

print("Hello, welcome to quadratic solver")
a = request.form['a']
b = request.form['b']
c = request.form['c']
print(a, b, c)

sq = sqrt(b*b - 4*a*c)
print(eval("(%s - %s)/(2*%s)" % (-b, sq, a)))

#print("Your result is: "+str(calculate(a, b, c)[0])+", "+str(calculate(a, b, c)[1]))
