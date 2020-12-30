from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):

        data = "Fibonacci Sequence"
        return jsonify({'data': data})

def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print('Incorrect input')
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(21))

if __name__ == '__main__':
    app.run(debug = True)
