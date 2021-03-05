from math import sqrt

print("Hello, welcome to quadratic solver")
a = input("Type value for a: ")
b = input("Type value for b: ")
c = input("Type value for c: ")
print(a, b, c)

sq = sqrt(b*b - 4*a*c)
print(eval("(%s - %s)/(2*%s)" % (-b, sq, a)))

def calculate(a, b, c):
    sq = sqrt(b*b - 4*a*c)
    result = lambda op: eval("(%s %s %s)/(2*%s)" % (-b, op, sq, a))
    return [result("-"), result("+")]

print("Your result is: "+str(calculate(a, b, c)[0])+", "+str(calculate(a, b, c)[1]))
